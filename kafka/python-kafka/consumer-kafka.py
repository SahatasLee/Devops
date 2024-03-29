from kafka import KafkaConsumer
import zstandard as zstd

BOOTSTRAP_SERVERS = ['10.111.0.125:9094']
SECURITY_PROTOCOL = 'SASL_PLAINTEXT'
SASL_MECHANISM = 'SCRAM-SHA-512'
SASL_PLAIN_USERNAME = 'user-test'
SASL_PLAIN_PASSWORD = 'dNam4SJtKb81'

try:
    consumer = KafkaConsumer(
                            #  "topic-test", 
                            #  api_version=(0, 8, 0),
                            bootstrap_servers=BOOTSTRAP_SERVERS,
                            consumer_timeout_ms=10000, # StopIteration if no message after 10 sec 
                            security_protocol=SECURITY_PROTOCOL, #used to communicate with brokers
                            sasl_mechanism=SASL_MECHANISM,
                            sasl_plain_username=SASL_PLAIN_USERNAME,
                            sasl_plain_password=SASL_PLAIN_PASSWORD,
                            auto_offset_reset='earliest', 
                            enable_auto_commit=False,
                            value_deserializer=lambda x: x.decode('utf-8'),
                            key_deserializer=lambda x: x.decode('utf-8'),
                            group_id="group-test"
                            )

    # print("Connecting bootstrap", consumer.bootstrap_connected())
    if consumer.bootstrap_connected():
        print("Connection success")
        # consumer.assign({0, 1, 2})
        # print(consumer.subscription())
        consumer.subscribe(topics=["topic-test"])
        # print(consumer.beginning_offsets())
        print("Subscribed to topic:", consumer.subscription())
        print("Topics", consumer.topics())
        print('Partitions for topic',consumer.partitions_for_topic('topic-test'))
        print('Get the TopicPartitions currently assigned to this consumer',consumer.assignment())
        print('Return True if this consumer can/should join a broker-coordinated group.', consumer._use_consumer_group())
        print('Fetch data from assigned topics / partitions.',consumer.poll())
        for message in consumer:
            print(message)
            # message value and key are raw bytes -- decode if necessary!
            # e.g., for unicode: `message.value.decode('utf-8')`
            print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                                    message.offset, message.key,
                                                    message.value))
    else:
        print("Connection failed")
            
    consumer.close()
    print("Connection close")


except Exception as e:
    print (e)