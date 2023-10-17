# Topic Kafka

## YAML

```bash
apiVersion: kafka.strimzi.io/v1beta2 
kind: KafkaTopic 
metadata: 
    name: eaadmin 
    labels: 
        strimzi.io/cluster: kafka-cluster-poc 
spec: 
    partitions: 3 
    replicas: 3 
    config: 
        retention.ms: 604800000 
        cleanup.policy: compact, delete 
        compression.type: zstd 
```

## What is difference between partition and replica of a topic in kafka cluster?

[Stackoverflow](https://stackoverflow.com/questions/27150925/what-is-difference-between-partition-and-replica-of-a-topic-in-kafka-cluster)

When you add the message to the topic, you call send(KeyedMessage message) method of the producer API. This means that your message contains key and value. When you create a topic, you specify the number of partitions you want it to have. When you call "send" method for this topic, the data would be sent to only ONE specific partition based on the hash value of your key (by default). Each partition may have a replica, which means that both partitions and its replicas store the same data. The limitation is that both your producer and consumer work only with the main replica and its copies are used only for redundancy.

Refer to the documentation: http://kafka.apache.org/documentation.html#producerapi And a basic training: http://www.slideshare.net/miguno/apache-kafka-08-basic-training-verisign