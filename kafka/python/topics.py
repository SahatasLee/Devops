
f = open("topics.txt", "r")

topic_list = []

for topic in f:
    if topic != '\n':
        topic_list.append(topic.strip('\n'))

print(topic_list)

# Define the YAML template
yaml_template = """
---
apiVersion: kafka.strimzi.io/v1beta2
kind: KafkaTopic
metadata:
  name: {topic_name}
  labels:
    strimzi.io/cluster: kafka-cluster-dev
spec:
  partitions: 3
  replicas: 3
  config:
    retention.ms: 604800000
    cleanup.policy: compact,delete
    compression.type: zstd
"""

# Generate YAML files 
yaml_files = ""
for topic in topic_list:
    yaml_content = yaml_template.format(topic_name=topic)
    yaml_files += yaml_content

f = open('topics.yaml', 'w')
f.write(yaml_files)
f.close()

print(yaml_files)

