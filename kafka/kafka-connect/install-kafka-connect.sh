#!/bin/bash

# Create Secret to login to registry
kubectl create secret -n kafka docker-registry secret-docker --docker-server="container registry url" --docker-username="username" --docker-password="password"
# Create Secrect for username
kubectl apply -n kafka -f connect-user.yml
# get connect-user password to sc-connect.txt
sleep 5
kubectl get secret connect-user -n kafka --template={{.data}} | cut -d ":" -f 2 | base64 -d > sc-connect.txt
# create Secret for Password
kubectl create secret -n kafka generic sc-connect-user --from-file=password=sc-connect.txt
# Create Kafka Connect 
kubectl apply -n kafka -f kafka-connect.yml