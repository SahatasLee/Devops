# Kafdrop

create password run file get-kafka-user-pasword.sh

    get-kafka-user-pasword.sh

create file **kafkapoc.properties**

```Bash
security.protocol=SASL_PLAINTEXT
sasl.mechanism=SCRAM-SHA-512 
sasl.jaas.config=org.apache.kafka.common.security.scram.ScramLoginModule required \
username="kafdrop-user" \
password="Vpi8KF5pMxeu"; 
#change password to yr own password and user
```

run kafdrop on ansible node
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

```Bash
# for check image is running
docker ps
```