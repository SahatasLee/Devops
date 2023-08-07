# Kafka

Kafka installation manual

## Requirement

- kubernetes cluster
- nfs server

## Installation

1. Install kafka operator

    create kafka namespace

        kubectl create ns kafka

    install strimzi

        helm repo add strimzi <https://strimzi.io/charts/>
        helm repo update

    install kafka-cluster-operator defualt is lastest version

        helm install kafka-cluster strimzi/strimzi-kafka-operator --namespace kafka

    can specify version by this command

        helm install kafka-cluster strimzi/strimzi-kafka-operator --version 0.26.0 --namespace kafka

    Scale replicas

    ```bash
    kubectl scale deployments/strimzi-cluster-operator  --replicas=3 -n kafka
    ```

    wait until pod stimzi-cluster-operator is complete

    config ip loadbalancer and storage class in kafka-cluster/kafka-cluster.yaml

    ```yaml
    bootstrap:
        loadBalancerIP: 10.111.0.28 # change here
    brokers:
    - broker: 0
        loadBalancerIP: 10.111.0.29 # change here
    - broker: 1
        loadBalancerIP: 10.111.0.30 # change here
    - broker: 2
        loadBalancerIP: 10.111.0.31 # change here
    ```

    and storage class line 68, 108 change to your pvc

2. Create kafdrop-user

    1. prepare file `kafdrop-user.yaml`

    ```yaml
    apiVersion: kafka.strimzi.io/v1beta1
    kind: KafkaUser
    metadata:
    name: kafdrop-user # username
    labels:
        strimzi.io/cluster: kafka-cluster-poc
    spec:
    authentication:
        type: scram-sha-512
    authorization:
        type: simple
        acls:
        - resource:
            type: topic
            name: '*'
            patternType: literal
            operation: All
        - resource:
            type: cluster
            name: '*'
            patternType: literal
            operation: All
        - resource:
            type: group
            name: '*'
            patternType: literal
            operation: All
        - resource:
            type: transactionalId
    ```

    2. create user

    ```Bash
    kubectl -n kafka apply -f kafdrop-user.yaml
    ```

    3. get password [get-kafka-user-password.sh](get-kafka-user-pasword.sh)

    ```Bash
    bash get-kafka-user-pasword.sh
    ```

    4. go to `anisible server` and create `kafkapoc.propoties` file

    ```Bash
    security.protocol=SASL_PLAINTEXT
    sasl.mechanism=SCRAM-SHA-512 
    sasl.jaas.config=org.apache.kafka.common.security.scram.ScramLoginModule required 
    username="kafdrop-user"
    password="Vpi8KF5pMxeu"; 
    #change password to yr own password and user
    ```

    5. install docker

    ```Bash
    apt install docker -y && apt install docker.io -y
    ```

    6. run docker

    ```Bash
    docker run -d --rm -p 9039:9000 \
        -e KAFKA_BROKERCONNECT=10.111.0.128:9094 \
        -e KAFKA_PROPERTIES="$(cat kafkapoc.properties | base64)" \
        -e JVM_OPTS="-Xms32M -Xmx64M" \
        -e SERVER_SERVLET_CONTEXTPATH="/" \
        -e CMD_ARGS="--topic.deleteEnabled=false --topic.createEnabled=false" \
        -v /etc/localtime:/etc/localtime:ro \
        obsidiandynamics/kafdrop
    ```
