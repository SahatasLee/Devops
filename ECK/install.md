# ECK

1. Install custom resource definitions:

        kubectl create -f https://download.elastic.co/downloads/eck/2.6.1/crds.yaml

    The following Elastic resources have been created:

        customresourcedefinition.apiextensions.k8s.io/agents.agent.k8s.elastic.co created
        customresourcedefinition.apiextensions.k8s.io/apmservers.apm.k8s.elastic.co created
        customresourcedefinition.apiextensions.k8s.io/beats.beat.k8s.elastic.co created
        customresourcedefinition.apiextensions.k8s.io/elasticmapsservers.maps.k8s.elastic.co created
        customresourcedefinition.apiextensions.k8s.io/elasticsearches.elasticsearch.k8s.elastic.co created
        customresourcedefinition.apiextensions.k8s.io/enterprisesearches.enterprisesearch.k8s.elastic.co created
        customresourcedefinition.apiextensions.k8s.io/kibanas.kibana.k8s.elastic.co created

2. Install the operator with its RBAC rules:

        kubectl apply -f https://download.elastic.co/downloads/eck/2.6.1/operator.yaml

    The ECK operator runs by default in the elastic-system namespace. It is recommended that you choose a dedicated namespace for your workloads, rather than using the elastic-system or the default namespace.

3. Monitor the operator logs:

        kubectl -n elastic-system logs -f statefulset.apps/elastic-operator

    From <https://www.elastic.co/guide/en/cloud-on-k8s/current/k8s-deploy-eck.html>

    Install Kibana, Fleet & Elastic search

        kubectl apply -f elastic-kibana-fleet.yaml

    Edit svc of Kibana, Elasticsearch-http, fleet-server-http to LB

        kubectl apply -f apm-server.yaml

4. Access to Kibana

    Get secret to login to kibana

        kubectl get secret elasticsearch-es-elastic-user -o=jsonpath='{.data.elastic}' | base64 --decode; echo

    User : elastic
    Pass : from secret above
