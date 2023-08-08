# Kafka Connect

Install manual

## Install

1. Config [install-kafka-connect.sh](install-kafka-connect.sh)

    ```Bash
    kubectl create secret -n kafka docker-registry secret-docker --docker-server="container registry url" --docker-username="username" --docker-password="password"
    ```
    * docker-username is email or username
    * docker-passowrd is password or access token if you use 2fac authen you need access token instead of password.

2. Config [connect-user.yaml](connect-user.yaml)

    ```yaml
    metadata:
        name: connect-user
        labels:
            strimzi.io/cluster: kafka-poc # here
    ```

3. Config [kafka-connect.yaml](kafka-connect.yaml)

    * name
    * ip
    * image registry

4. Run script [install-kafka-connect.sh](install-kafka-connect.sh)

    ```Bash
    bash install-kafka-connect.sh
    ```