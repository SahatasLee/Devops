from kafka import KafkaProducer #!!!!!
import zstandard as zstd

 

bootstrap_servers = ['10.111.0.107:9094']
security_protocol = 'SASL_PLAINTEXT'
sasl_mechanism = 'SCRAM-SHA-512'
sasl_plain_username = 'usertest'
sasl_plain_password = 'RgRgCmzmqNueSjb3ceWDaTlfCEI60yLQ'

 


# Create Kafka producer instance
producer = KafkaProducer(
    bootstrap_servers=bootstrap_servers, #เอาไว้ให้consumerเชื่อมกับbooststrapได้
    api_version=(2,1,0),
    max_block_ms = 60000 ,
    security_protocol=security_protocol, #used to communicate with brokers
    sasl_mechanism=sasl_mechanism,
    sasl_plain_username=sasl_plain_username,
    sasl_plain_password=sasl_plain_password,
    value_serializer=lambda x: zstd.ZstdCompressor(level=3).compress(x.encode('utf-8')),
    key_serializer=lambda x: str(x).encode('utf-8'),
    compression_type='zstd'
)

 

# Produce a message to a Kafka topic with a key
topic = 'topic-test' #เปลี่ยนชื่อ
message = 'Hello, Kafka!'
print("connected bootstrap: " +str( producer.bootstrap_connected()))
num_loops = int(input("Enter the number of times to loop: "))
for i in range(num_loops):
    key = i
   # print('Message sent to Kafka: ', message)

    producer.send(topic, key=key, value=message)
    print('Message sent to Kafka: ', message)

 

# Wait for any outstanding messages to be transmitted and delivery reports received
producer.flush()

 

# Close the producer instance
producer.close()