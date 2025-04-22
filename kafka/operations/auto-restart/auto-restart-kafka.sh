#!/bin/bash
# Script auto restart kafka connectors
# Written by Sahatas.L

# Get connect pod
pod=$(kubectl -n kafka get po | grep kafka-connect-prd-connect | head -n 1 | awk '{print $1}')
# Copy script to pod
kubectl -n kafka cp check-failed-connectors.sh $pod:/tmp/
# Copy script to pod
kubectl -n kafka cp restart-loops-kctr.sh $pod:/tmp/
# Change permission in pod
# kubectl -n kafka exec -it $pod -- /bin/bash -c "chmod 777 /tmp/check-failed-connectors.sh"
# Run check failed connectors script in pod
kubectl -n kafka exec -it $pod -- /bin/bash -c "bash /tmp/check-failed-connectors.sh"
#
# kubectl -n kafka exec -it $pod -- /bin/bash -c "cat /tmp/all_connectors.txt" > all_connectors.txt
# Copy file to pod and Restart connectors
kubectl -n kafka exec -it $pod -- /bin/bash -c "cp /tmp/failed_connector.txt /tmp/connectors.txt && bash /tmp/restart-loops-kctr.sh"
#
echo "restart connector done"