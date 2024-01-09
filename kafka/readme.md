# Kafka

Kafka installation manual

https://strimzi.io/

https://strimzi.io/blog/2018/11/01/using-helm/

## Requirement

- kubernetes cluster
- storage class

## Installation

1. Install kafka operator

    1. create kafka namespace

    ```bash
    kubectl create ns kafka
    ```

    2. install strimzi

    ```bash
    helm repo add strimzi https://strimzi.io/charts/
    helm repo update
    ```

    3. install kafka-cluster-operator defualt is lastest version

    ```bash
    helm install kafka-cluster strimzi/strimzi-kafka-operator --namespace kafka
    ```

    can specify version by this command

    ```bash
    helm install kafka-cluster strimzi/strimzi-kafka-operator --version 0.26.0 --namespace kafka
    ```

    Install 2 namespace

    ```
    helm install kafka-cluster strimzi/strimzi-kafka-operator \
    --namespace kafka \
    --set watchNamespaces="{kafka-nut}" \
    --version 0.26.0 \
    ```

    Add a namepaces

    ```
    helm upgrade \
    --reuse-values \
    --set watchNamespaces="{kafka-nut}" \
    kafka-cluster strimzi/strimzi-kafka-operator
    ```

    Scale replicas

    ```bash
    kubectl scale deployments/strimzi-cluster-operator  --replicas=3 -n kafka
    ```

    wait until pod stimzi-cluster-operator is complete

    config ip loadbalancer and storage class in `kafka-cluster/kafka-cluster.yaml`

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

    [kafka-cluster-poc](kafka-cluster/kafka-cluster-poc.yml)

    ```Bash
    # apply kafka-cluster folder
    kubectl -n kafka apply -f kafka-cluster/
    ```

    Output

    ```Bash
    root@node1:~# kubectl -n kafka apply -f kafka/kafka-cluster/
    kafka.kafka.strimzi.io/kafka-cluster-poc created
    configmap/kafka-metrics created
    configmap/zookeeper-metrics created
    ```

## Create kafdrop-user (admin) && Docker Kafdrop

1. prepare file [kafdrop-user.yaml](\kafdrop\kafdrop-user.yml)

```yaml
apiVersion: kafka.strimzi.io/v1beta1
kind: KafkaUser
metadata:
  name: kafdrop-user
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
          name: '*'
          patternType: literal
        operation: All
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
    sasl.jaas.config=org.apache.kafka.common.security.scram.ScramLoginModule required \
    username="kafdrop-user" \
    password="Vpi8KF5pMxeu";
    
    #change password to yr own password and user
    ```
    Example [link](https://github.com/instaclustr/sample-KafkaSparkCassandra/blob/master/kafka.properties.template)

5. install docker

    ```Bash
    apt install docker -y && apt install docker.io -y
    ```

6. run docker

    change `KAFKA_BROKERCONNECT=10.111.0.128:9094` to your boostrap ip

    ```Bash
    docker run -d --rm -p 9039:9000 \
        -e KAFKA_BROKERCONNECT=10.111.0.124:9094 \
        -e KAFKA_PROPERTIES="$(cat kafkapoc.properties | base64)" \
        -e JVM_OPTS="-Xms32M -Xmx64M" \
        -e SERVER_SERVLET_CONTEXTPATH="/" \
        -e CMD_ARGS="--topic.deleteEnabled=false --topic.createEnabled=false" \
        -v /etc/localtime:/etc/localtime:ro \
        obsidiandynamics/kafdrop
    ```

## Upgrade Kafka using 

1. Helm upgrade strimzi-operator

    ```bash
    helm upgrade kafka-cluster strimzi/strimzi-kafka-operator --namespace kafka
    ```

2. Change version kafka cluster 

    `version`

    ```yaml
    apiVersion: kafka.strimzi.io/v1beta2
    kind: Kafka
    metadata:
        name: kafka-cluster-poc
    spec:
        kafka:
            version: 3.4.0 
            logging:
                type: inline
    ```

    `log.message.format.version: "2.8"`
    
    `inter.broker.protocol.version: "2.8"`

    ```yaml
    config:
      default.replication.factor: 3
      min.insync.replicas: 3
      offsets.topic.replication.factor: 3
      transaction.state.log.replication.factor: 3
      transaction.state.log.min.isr: 2
      log.message.format.version: "2.8"
      inter.broker.protocol.version: "2.8"
    ```