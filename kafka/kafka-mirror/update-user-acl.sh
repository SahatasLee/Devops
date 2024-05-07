#!/bin/bash
# This script was written by Jaturong.S

# Setting up ENV
DIR="/home/eaadmin/kafkamirror/user/"
SOURCE_HOST="kafka-dc-01"
TARGET_HOST="kafka-dr-01"
SOURCE_CLUSTER="kafka-dc"
TARGET_CLUSTER="kafka-dr"
echo "Please input Kafkauser"
read kafka_user
KAFKA_USER=THAIBEV-KAFKAUSER-$(echo $kafka_user | tr [:lower:] [:upper:])
FILE="$KAFKA_USER.yml"
FILE_DR="$KAFKA_USER-DR.yml"

# Updating YML file and apply Kafka configuration local
if [ -e $DIR$FILE ]; then
	echo "<-- Applying Kafkauser to $SOURCE_CLUSTER -->"
	kubectl -n kafka apply -f $DIR$FILE
	echo "-----------------------------------------------------------------------------"
	sleep 1
else 
	echo "[FAILED]: Please check $FILE is exist in $DIR"
	exit 1
fi

# Changing target cluster YML file with sed and apply user to target host
sed "s/$SOURCE_CLUSTER/$TARGET_CLUSTER/g" "$DIR$FILE" > $DIR$FILE_DR
sleep 2
echo "<-- Updating target YML file and applying kafkauser to $TARGET_CLUSTER -->"
scp $DIR$FILE_DR $TARGET_HOST:$DIR.
sleep 1
ssh $TARGET_HOST kubectl -n kafka apply -f $DIR$FILE_DR
echo "-----------------------------------------------------------------------------"

# Cleaning up dr file
rm -f $DIR$FILE_DR
if [ $? -eq 0 ]; then
	echo "[COMPLETED]: Kafkauser has been updated"
	exit 0
else
    echo "[FAILED]: Cannot update Kafkauser"
	exit 1
fi
