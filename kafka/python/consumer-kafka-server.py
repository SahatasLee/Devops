from kafka import KafkaConsumer
import zstandard as zstd

bootstrap_servers = '10.7.37.202:9094'
security_protocol = 'SASL_PLAINTEXT'
sasl_mechanism = 'SCRAM-SHA-512'
sasl_plain_username = 'ea-test'
sasl_plain_password = 'BalN5xG1ba62'
topic = 'ea-topic-test'
group_id = "ea-group-test"
decompressor = zstd.ZstdDecompressor()

# Create a Kafka consumer instance
consumer = KafkaConsumer(
    topic,
    group_id=group_id,
    bootstrap_servers=bootstrap_servers,
    security_protocol=security_protocol,
    sasl_mechanism=sasl_mechanism,
    sasl_plain_username=sasl_plain_username,
    sasl_plain_password=sasl_plain_password,
    auto_offset_reset='earliest', # start consuming from the earliest offset
    enable_auto_commit=True, # commit offsets automatically
    key_deserializer=lambda x: x.decode('utf-8'),
    value_deserializer=lambda x: decompressor.decompress(x).decode('utf-8'),
    consumer_timeout_ms=1000
)

# Consume messages from the Kafka topic
for message in consumer:
    print(f"Received message: {message.value} with key {message.key}")
