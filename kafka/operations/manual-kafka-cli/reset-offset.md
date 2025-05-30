# Reset Offset

## prerequisite

1. `user.properties`

```sh
kubectl -n kafka get po
kubectl -n kafka cp user.properties kafka-pod-0:/tmp/user.properties
kubectl -n kafka exec -it kafka-pod-0 -- bash
# List topics
./bin/kafka-topics.sh --bootstrap-server bootstrap-ip:9092 --list --command-config /tmp/user.properties
# Reset offset
./bin/kafka-consumer-groups.sh --bootstrap-server bootstrap-ip:9092 --group consumer-group --reset-offsets --command-config /tmp/user.properties --to-earliest --topic topic-name --execute
```
