#!/bin/bash

# Script to restart kafka connectors
# Written by Sahatas.L

# Assuming connectors.txt contains the list of connectors to restart (one per line)
input_file="connectors.txt"

# Check if file exists
if [[ ! -f "$input_file" ]]; then
    echo "File '$input_file' not found!"
    exit 1
fi

# Loop through each line (connector name) in the file
while IFS= read -r connector || [[ -n "$connector" ]]; do

    url="http://localhost:8083/connectors/$connector/"

    response=$(curl --head --write-out %{http_code} --silent --output /dev/null "$url")

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
