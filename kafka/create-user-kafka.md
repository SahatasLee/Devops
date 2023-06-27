# Create User Kafka

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

apply

    kubectl apply -f (your file) -n kafka 

output

    kafkauser.kafka.strimzi.io/test-user created

Check

    kubectl get ku –n kafka

Get kafka password

Create **get-kafka-user-password.sh**

    #!/bin/bash 

    echo "Please input Kafka User" 

    read kafka_user 

    kubectl get secret $kafka_user -n kafka --template={{.data}} | cut -d ":" -f 3 | base64 -d

get password

    bash get-kafka-user-password.sh 

save password to txt file and lock
