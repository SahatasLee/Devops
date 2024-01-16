import sys
from confluent_kafka import Consumer, KafkaError, KafkaException
import zstandard as zstd

BOOTSTRAP_SERVERS = '10.111.0.124:9094'
SECURITY_PROTOCOL = 'SASL_PLAINTEXT'
SASL_MECHANISM = 'SCRAM-SHA-512'
SASL_PLAIN_USERNAME = 'ea-test'
SASL_PLAIN_PASSWORD = 'BalN5xG1ba62'

try:
    conf = {
        'bootstrap.servers': BOOTSTRAP_SERVERS,
        'security.protocol': SECURITY_PROTOCOL,
        'sasl.mechanism': SASL_MECHANISM,
        'sasl.username': SASL_PLAIN_USERNAME,
        'sasl.password': SASL_PLAIN_PASSWORD,
        'group.id': 'ea-group-test',
        'auto.offset.reset': 'smallest',
        'enable.auto.commit': 'false',
        }

    consumer = Consumer(conf)
    running = True
    consumer.subscribe(["topic-test"])
    count = 0
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None: 
            # Initial message consumption may take up to
            # `session.timeout.ms` for the consumer group to
            # rebalance and start consuming
            print("Waiting...")

        elif msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # End of partition event
                sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                    (msg.topic(), msg.partition(), msg.offset()))
            elif msg.error():
                raise KafkaException(msg.error())
        else:
            # print("Consumed event from topic {topic}: key = {key} value = {value}".format(
            #         topic=msg.topic(), key=msg.key(), value=msg.value()))
            print("Consumed event from topic {topic}: key = {key:12} value = {value:12}".format(
                    topic=msg.topic(),
                    key=msg.key().decode('utf-8'),
                    value=zstd.ZstdDecompressor().decompress(msg.value()).decode('utf-8')
                ))
            count += 1
            print("Count", count)

except KeyboardInterrupt:
    pass
finally:
    # Leave group and commit final offsets
    consumer.close()