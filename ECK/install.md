# ECK

1. Install custom resource definitions:

    ```bash
    kubectl create -f https://download.elastic.co/downloads/eck/2.6.1/crds.yaml
    ```

    The following Elastic resources have been created:

    ```bash
    customresourcedefinition.apiextensions.k8s.io/agents.agent.k8s.elastic.co created
    customresourcedefinition.apiextensions.k8s.io/apmservers.apm.k8s.elastic.co created
    customresourcedefinition.apiextensions.k8s.io/beats.beat.k8s.elastic.co created
    customresourcedefinition.apiextensions.k8s.io/elasticmapsservers.maps.k8s.elastic.co created
    customresourcedefinition.apiextensions.k8s.io/elasticsearches.elasticsearch.k8s.elastic.co created
    customresourcedefinition.apiextensions.k8s.io/enterprisesearches.enterprisesearch.k8s.elastic.co created
    customresourcedefinition.apiextensions.k8s.io/kibanas.kibana.k8s.elastic.co created
    ```

2. Install the operator with its RBAC rules:

    ```bash
    kubectl apply -f https://download.elastic.co/downloads/eck/2.6.1/operator.yaml
    ```

    The ECK operator runs by default in the elastic-system namespace. It is recommended that you choose a dedicated namespace for your workloads, rather than using the elastic-system or the default namespace.

3. Monitor the operator logs:

    ```bash
    kubectl apply -f https://download.elastic.co/downloads/eck/2.6.1/operator.yaml
    ```

    From <https://www.elastic.co/guide/en/cloud-on-k8s/current/k8s-deploy-eck.html>

    Install Kibana, Fleet & Elastic search

    ```bash
    kubectl apply -f elastic-kibana-fleet.yaml
    ```

    Edit svc of Kibana, Elasticsearch-http, fleet-server-http to LB

    ```bash
    kubectl apply -f apm-server.yaml
    ```

4. Access to Kibana

    Get secret to login to kibana

    ```bash
    kubectl get secret elasticsearch-es-elastic-user -o=jsonpath='{.data.elastic}' | base64 --decode; echo
    ```

    User : elastic
    
    Pass : from secret above

5. URL

    Test Kibana

    ```bash
    curl -u "elastic:$PASSWORD" -k "https://10.111.0.120:5601"
    ```

    Test Elastic

    ```bash
    curl "https://10.111.0.121:9200" -k -u "elastic:$PASSWORD"
    ```

    >Note: neet to type https://

6. CA

    Note : this happens only self signed certificate on elastic

    Copy file cert from pod elasticsearch

    ```
    kubectl cp elasticsearch-es-default-0:/usr/share/elasticsearch/config/http-certs/..data/ca.crt /tmp/ca.crt
    ```
    Then winscp to copy file ca.crt

    Then copy the ca.crt to Agent server and install cert as trusted

    Edit elasticagent.yaml below

    outputs:
    default:
        type: elasticsearch
        hosts: ["https://xx.xx.xx.xx:9200"]
        ssl.certificate_authorities: ["c:/eck/certs/ca.crt"]

    output.elasticsearch:
    # Array of hosts to connect to.
    hosts: ["https://10.195.100.125:9200"]
    ssl.certificate_authorities: ["c:/eck/certs/ca.crt"]

    Restart Elastic Agent and check the metric beat & filebeat log

    "message":"Connection to backoff(elasticsearch(https://10.195.100.125:9200)) established","service.name":"metricbeat","ecs.v

7. Delete

    ```bash
    kubectl delete -f elastic-kibana-fleet.yaml -f apm-server.yaml
    ```

## Demo

https://github.com/elastic/opentelemetry-demo/blob/main/README.md