# Create User Kafka
```Yaml
## KAFKAUSER-ADMPPEX ## 
--- 
apiVersion: kafka.strimzi.io/v1beta2 
kind: KafkaUser 
metadata: 
  name: admppex 
  labels: 
    strimzi.io/cluster: kafka-cluster-poc 
spec: 
  authentication: 
    type: scram-sha-512 
  authorization: 
    type: simple 
    acls: 
      # access to kafka topic [Write] 
      - resource: 
          type: topic 
          name: eaadmin 
          patternType: literal 
        operation: All 
        host: "*" 
      # access to kafka group [All] 
      - resource: 
          type: group 
          name: group-eaadmin 
          patternType: literal 
        operation: All 
        host: "*" 
```

1. Apply

    ```Bash
    kubectl apply -f (your file) -n kafka 
    ```

    output

    ```Bash
    kafkauser.kafka.strimzi.io/test-user created
    ```

2. Check

    ```Bash
    kubectl get ku <your user> –n kafka
    ```

3. Get kafka password

    Create `get-kafka-user-password.sh`

    ```Bash
    #!/bin/bash 
    echo "Please input Kafka User" 
    read kafka_user 
    kubectl get secret $kafka_user -n kafka --template={{.data}} | cut -d ":" -f 3 | base64 -d
    ```

    run script

    ```Bash
    bash get-kafka-user-password.sh 
    ```

    save password to txt file, zip and lock
