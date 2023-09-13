# Create kafka Connector

![Alt text](./images/email-connector-request.png)

1. Download .zip file and unzip
2. Copy `request folder` to `kafka-debezium` folder on ea-step-server
3. Rename a request folder to Upper Letter and click in

    folder name example: **OMHAS**

4. Create a folder names created date and click in

    folder name example: **31-JUL**

5. Create folder

    folder name example: **"1-connector-otc-omhas-omsap-omhas-domainproduct"**

6. Copy old connector yml file and paste or pattern like `connector-otc-omhas-omsap-omhas-domainproduct.yaml`
7. Rename old file to requested yml file

    ![Alt text](./images/connector-request.png)

    file name `connector-otc-omhas-omsap-omhas-domainproduct.yaml`

8. Config

    ```yml
    apiVersion: kafka.strimzi.io/v1beta2
    kind: KafkaConnector
    metadata:
    name: name # rename
    labels:
        strimzi.io/cluster: kafka-connect-prd
    spec:
    class: io.debezium.connector.sqlserver.SqlServerConnector
    tasksMax: 1
    config:
        database.hostname: 127.0.0.1 # here
        database.port: "1433" # here
        database.user: "admin" # here
        database.password: "12341234" # here
        database.dbname: "sap" # here
        database.server.name: "o-sap" # here
        database.history.kafka.topic: "o-sap" # here
        table.include.list: "something" # here
        transforms.route.replacement: "sth" # here
    ```
