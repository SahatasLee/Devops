from kafka import KafkaProducer #!!!!!
import zstandard as zstd

BOOTSTRAP_SERVERS = ['10.111.0.125:9094']
security_protocol = 'SASL_PLAINTEXT'
sasl_mechanism = 'SCRAM-SHA-512'
sasl_plain_username = 'user-test'
sasl_plain_password = 'dNam4SJtKb81'

# Create Kafka producer instance
producer = KafkaProducer(
    bootstrap_servers=BOOTSTRAP_SERVERS, #เอาไว้ให้consumerเชื่อมกับbooststrapได้
    # api_version=(2,1,0),
    max_block_ms = 60000 ,
    security_protocol=security_protocol, #used to communicate with brokers
    sasl_mechanism=sasl_mechanism,
    sasl_plain_username=sasl_plain_username,
    sasl_plain_password=sasl_plain_password,
    value_serializer=lambda x: zstd.ZstdCompressor(level=3).compress(x.encode('utf-8')),
    key_serializer=lambda x: str(x).encode('utf-8'),
    compression_type='zstd'
)
print("connected bootstrap: " + str(producer.bootstrap_connected()))

# Produce a message to a Kafka topic with a key
topic = 'topic-test' #เปลี่ยนชื่อ
message = 'Hello, Kafka! Produce messages from python.'
num_loops = int(input("Enter the number of times to loop: "))
for i in range(num_loops):
    key = i
    producer.send(topic, key=key, value=str(message + " Number: " + str(i)))
    print('Message sent to Kafka: ', str(message + " Number: " + str(i)))

# Wait for any outstanding messages to be transmitted and delivery reports received
producer.flush()

# Close the producer instance
producer.close()