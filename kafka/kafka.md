# Kafka

---

## Requirement

---

- kubernetes cluster
- nfs server

## Installation

---

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

    kubectl scale deployments/strimzi-cluster-operator  --replicas=3 -n kafka

wait until pod stimzi-cluster-operator is complete

config ip loadbalancer and storage class in kafka-cluster/kafka-cluster.yaml

    bootstrap:
        loadBalancerIP: 10.111.0.28 # change here
    brokers:
    - broker: 0
        loadBalancerIP: 10.111.0.29 # change here
    - broker: 1
        loadBalancerIP: 10.111.0.30 # change here
    - broker: 2
        loadBalancerIP: 10.111.0.31 # change here

and storage class line 68, 108 change to your pvc
