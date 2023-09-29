# Reset connector

1. exec connect pod

```bash
kubectl exec -it -n kafka kafka-connect-prd-connect-5dfff8b7d7-kgc4b -- /bin/bash
```

2. run `bash reset.sh`

```bash
#Script to restart kafka connectors
#Written by Jaturong.S

echo 'Please input connector name:'
read connector

url="http://localhost:8083/connectors/$connector/"


response=$(curl --head --write-out %{http_code} --silent --output /dev/null $url)


#main
if [[ $response -ne 200 ]]
then
        echo "Connector '$connector' not found please try again"
        exit 1
else
        echo '===> Connector is pausing...'
        curl -X PUT http://localhost:8083/connectors/$connector/pause
        sleep 3
        echo '===> Connector is restarting...'
        curl -X POST http://localhost:8083/connectors/$connector/restart
        sleep 3
        curl -X POST http://localhost:8083/connectors/$connector/tasks/0/restart
        sleep 3
        echo '===> Connector is resuming...'
        curl -X PUT http://localhost:8083/connectors/$connector/resume
        sleep 10
        echo '===> Connector has been restarted !!'
        curl -X GET http://localhost:8083/connectors/$connector/status | cut -d "," -f 2-6

        exit 0
fi
```

