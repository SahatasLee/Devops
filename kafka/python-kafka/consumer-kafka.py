from kafka import KafkaConsumer
import zstandard as zstd

BOOTSTRAP_SERVERS = ['10.111.0.125:9094']
SECURITY_PROTOCOL = 'SASL_PLAINTEXT'
SASL_MECHANISM = 'SCRAM-SHA-512'
SASL_PLAIN_USERNAME = 'user-test'
SASL_PLAIN_PASSWORD = 'dNam4SJtKb81'

consumer = KafkaConsumer(
                        #  "topic-test", 
                        #  group_id="group-test", 
                         bootstrap_servers=BOOTSTRAP_SERVERS,
                         consumer_timeout_ms=1000, # StopIteration if no message after 1sec 

                         security_protocol=SECURITY_PROTOCOL, #used to communicate with brokers
                         sasl_mechanism=SASL_MECHANISM,
                         sasl_plain_username=SASL_PLAIN_USERNAME,
                         sasl_plain_password=SASL_PLAIN_PASSWORD,
                         auto_offset_reset='earliest', 
                         enable_auto_commit=False,
                         value_deserializer=lambda x: x.decode('utf-8'),
                         key_deserializer=lambda x: x.decode('utf-8')
                         )

# print("Connecting bootstrap", consumer.bootstrap_connected())
if consumer.bootstrap_connected():
    print("Connection success")
    consumer.subscribe(topics="topic-test")
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