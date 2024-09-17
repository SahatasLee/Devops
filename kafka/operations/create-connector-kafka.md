# Create kafka Connector

1. Download `nut Iot 1.zip` file and unzip
2. Copy `request folder` to `\Kafka Configuration\PRD\Kafka-Debezium` and `\Kafka Configuration\Request Debezium\PRD` folder on ea-step-server
3. Rename a request folder to Upper Letter and click in

    folder name: `nut Iot 22.zip` > `NUT`
    
    example: `PRD\Kafka-Debezium\NUT\`

4. Create a folder names created date and click in

    folder name: `DATE-MONTH`
    
    example: `PRD\Kafka-Debezium\NUT\17-SEP\`

5. Create folder

```sh
# Example
PRD\Kafka-Debezium\NUT\17-SEP\1-connector-name\
PRD\Kafka-Debezium\NUT\17-SEP\2-connector-nut-domainproduct\
```

6. Copy old connector yml file and Rename. Pattern like `connector-name.yaml`

    File name: `connector-name.yaml`

    Example: `PRD\Kafka-Debezium\NUT\17-SEP\2-connector-nut-domainproduct\connector-nut-domainproduct.yaml`

7. Config

    ```yml
    apiVersion: kafka.strimzi.io/v1beta2
    kind: KafkaConnector
    metadata:
    name: connector-name # rename
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

8. Create Topic

    Locations: In same folder with connector.yaml

    File name: `topic-name.yaml`

    Example: `PRD\Kafka-Debezium\NUT\17-SEP\2-connector-nut-domainproduct\nut-domainproduct.yaml`

    ```yaml
    apiVersion: kafka.strimzi.io/v1beta2
    kind: KafkaTopic
    metadata:
        name: nut-domainproduct
    labels:
        strimzi.io/cluster: kafka-cluster-prd
    spec:
        partitions: 3
        replicas: 1
        config:
            compression.type: zstd
            retention.ms: 259200000
            cleanup.policy: compact,delete
    ```

9. Add Topic to exists user. `USER.yml`

10. Copy `2-connector-nut-domainproduct` folder and `USER.yml` to `KAFKA-CLUSTER` by winscp

```sh
kubectl -n kafka apply -f 2-connector-nut-domainproduct/
kubectl -n kafka apply -f USER.yml
kubectl -n kafka describe kctr connector-nut-domainproduct
```

11. Wait for Connectors **UP**

```sh
Status:
  Conditions:
    Last Transition Time:  2024-09-17T07:32:08.293693Z
    Status:                True
    Type:                  Ready
  Connector Status:
    Connector:
      State:      RUNNING
      worker_id:  10.233.118.89:8083
    Name:         connector-otc-vsms-vsmstbv-websurvey-uploadtargetcompanyproduct-new
    Tasks:
      Id:               0
      State:            RUNNING
      worker_id:        10.233.118.89:8083
    Type:               source
  Observed Generation:  1
  Tasks Max:            1
  Topics:
    nut-domainproduct # Topic Name
    domainproduct # Database Server Name
```