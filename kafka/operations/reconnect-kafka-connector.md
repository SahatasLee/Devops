# Reset connector


1. copy file connectors.txt to pod

```bash
kubectl -n kafka cp connectors.txt kafka-connect-prd-connect-5dfff8b7d7-crpg5:/tmp/
```

2. exec connect pod

```bash
kubectl exec -it -n kafka kafka-connect-prd-connect-5dfff8b7d7-crpg5 -- /bin/bash
cd /tmp
```

1. run `bash reset.sh`

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

```bash
# Check if file exists
if [[ ! -f "$input_file" ]]; then
    echo "File '$input_file' not found!"
    exit 1
fi

# Loop through each line (connector name) in the file

while IFS='' read -r connector || [[ -n "$connector" ]]; do
    connector=${connector//$'\r'/}
    url="http://localhost:8083/connectors/$connector/"
    response=$(curl --head --write-out %{http_code} --silent --output /dev/null "$url")
    echo "===> URL: $url"
    # main
    if [[ $response -ne 200 ]]; then
        echo "Connector '$connector' not found. Skipping to next..."
        continue
    else
        echo "===> Processing connector: $connector"
        echo '===> Connector is pausing...'
        curl -X PUT "${url}pause"
        sleep 3
        echo '===> Connector is restarting...'
        curl -X POST "${url}restart"
        sleep 3
        curl -X POST "${url}tasks/0/restart"
        sleep 3
        echo '===> Connector is resuming...'
        curl -X PUT "${url}resume"
        sleep 10
        echo '===> Connector has been restarted !!'
        curl -X GET "${url}status" | cut -d "," -f 2-6
        echo # Printing an empty line for clarity between connectors
    fi
done < "$input_file"

echo "All connectors processed."
```

