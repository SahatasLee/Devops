# create TOPICS

template = """      - resource:
          type: group
          name: {topic}
          patternType: literal
        operation: All
        host: "*"
"""

create_topic_template = """apiVersion: kafka.strimzi.io/v1beta2
kind: KafkaTopic
metadata:
  name: {topic}
  labels:
    strimzi.io/cluster: kafka-cluster-prd
spec:
  partitions: 3
  replicas: 3
  config:
    retention.ms: 604800000
    cleanup.policy: compact,delete
    compression.type: zstd
---
"""

with open('topics.txt', 'r') as file:
    # Read all lines from the file into a list
    topics = file.readlines()

topics = [topic.strip().replace(",", "") for topic in topics if topic != '\n']

output = ""

create_topic_output = ""

for topic in topics:
    # print(topic)
    output += template.format(topic=topic)
    create_topic_output += create_topic_template.format(topic=topic)

with open('add-topic.yaml', 'w') as file:
    file.write(output)

with open('topic.yaml', 'w') as file:
    file.write(create_topic_output)