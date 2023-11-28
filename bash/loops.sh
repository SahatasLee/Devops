# !/bin/bash

input_file="connectors.txt"

# Check if file exists
if [[ ! -f "$input_file" ]]; then
    echo "File '$input_file' not found!"
    exit 1
fi

while IFS= read -r connector || [[ -n "$connector" ]]; do
    connector=${connector//$'\r'/}
    echo $connector
    echo "start $connector end"
    url="http://localhost:8083/connectors/$connector/"
    echo "===> URL: $url"
    echo "===> Processing connector: $connector"
    echo '===> Connector is pausing...'
    echo "${url}pause"
    # sleep 3
    echo '===> Connector is restarting...'
    echo "$url""restart"
    # sleep 3
    echo "$url""tasks/0/restart"
    # sleep 3
    echo '===> Connector is resuming...'
    echo "$url""resume"
    # sleep 10
    echo '===> Connector has been restarted !!'
    echo "$url""status" | cut -d "," -f 2-6
    echo
done < "$input_file" 
echo "All connectors processed."