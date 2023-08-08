# CREATE KAFKATOPIC

1. Create `KAFKATOPIC.yml`

    ```Bash
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
    ```

2. Apply config

    ```Bash
    kubectl apply -f (your file) -n kafka
    ```

    Output:
    ```Bash
    kafkatopic.kafka.strimzi.io/topic-test created
    ```

3. Check

    ```Bash
    kubectl get kt –n kafka (topic-metaname)
    ```

    Output:

    ```Bash
    root@kafv35s1:/home/eaadmin# kubectl -n kafka get kt topic-test
    NAME          CLUSTER             PARTITIONS   REPLICATION FACTOR   READY
    topic-test   kafka-cluster-poc   3            3                    True
    ```