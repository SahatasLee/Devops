# Kafdrop

create password run file get-kafka-user-pasword.sh

    get-kafka-user-pasword.sh

create file **kafkapoc.properties**

    security.protocol=SASL_PLAINTEXT
    sasl.mechanism=SCRAM-SHA-512 
    sasl.jaas.config=org.apache.kafka.common.security.scram.ScramLoginModule required 
    username="kafdrop-user"
    password="Vpi8KF5pMxeu"; 
    #change password to yr own password and user

run kafdrop on ansible node

    docker run -d --rm -p 9035:9000 \
        -e KAFKA_BROKERCONNECT=10.111.0.66:9094 \ #change ip to yr kafka-external-boostrap
        -e KAFKA_PROPERTIES="$(cat kafkapoc.properties | base64)" \
        -e JVM_OPTS="-Xms32M -Xmx64M" \
        -e SERVER_SERVLET_CONTEXTPATH="/" \
        -e CMD_ARGS="--topic.deleteEnabled=false --topic.createEnabled=false" \
        -v /etc/localtime:/etc/localtime:ro \
        obsidiandynamics/kafdrop
    docker ps #for check image is running.