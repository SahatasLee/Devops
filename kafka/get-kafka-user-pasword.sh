#!/bin/bash

echo "Please input Kafka User"
read kafka_user

kubectl get secret $kafka_user -n kafka --template={{.data}} | cut -d ":" -f 3 | base64 -d
