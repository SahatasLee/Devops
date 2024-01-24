# Install Heartbeat

heartbeat version 8.11.2

## Kubernetes

https://www.elastic.co/guide/en/beats/heartbeat/current/running-on-kubernetes.html

## Docker

https://www.elastic.co/guide/en/beats/heartbeat/current/running-on-docker.html#_optional_verify_the_image

1. Run Docker

```bash
    docker run \
    --cap-add=NET_RAW \
    docker.elastic.co/beats/heartbeat:8.11.1 \
    setup -E setup.kibana.host=kibana:5601 \
    -E output.elasticsearch.hosts=["elasticsearch:9200"]
```

Example
```bash
    docker run \
    --cap-add=NET_RAW \
    docker.elastic.co/beats/heartbeat:8.11.1 \
    setup -E setup.kibana.host=kibana:5601 \
    -E output.elasticsearch.hosts=["10.111.0.121:9200"]
```

## Windows

https://www.elastic.co/guide/en/beats/heartbeat/current/heartbeat-installation-configuration.html

https://www.elastic.co/guide/en/beats/heartbeat/8.5/monitor-http-options.html

```bash
# window path
C:\Program Files\Heartbeat\heartbeat-8.11.2-windows-x86_64\heartbeat.yml
```

Type `discover`

## Check

> Note User Password is up to date.
> CA
> IP Host