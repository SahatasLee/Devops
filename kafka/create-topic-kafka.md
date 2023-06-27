# CREATE KAFKATOPIC

create **KAFKATOPIC.yml**

    apiVersion: kafka.strimzi.io/v1beta2 

    kind: KafkaTopic 

    metadata: 

        name: topic-test 

        labels: 

            strimzi.io/cluster: kafka-cluster-poc 

    spec: 

        partitions: 3 

        replicas: 3 

        config: 

            retention.ms: 604800000 

            cleanup.policy: compact, delete 

            compression.type: zstd 

apply config

    kubectl apply -f (your file) -n kafka

    kafkatopic.kafka.strimzi.io/topic-test created

Check

    kubectl get kt –n kafka (topic-metaname)

    root@kafv35s1:/home/eaadmin# kubectl -n kafka get kt topic-test
    NAME          CLUSTER             PARTITIONS   REPLICATION FACTOR   READY
    topic-test   kafka-cluster-poc   3            3                    True
