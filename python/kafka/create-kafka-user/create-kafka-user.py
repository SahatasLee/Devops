# CREATE USER TEMPLATE

topic_template = """      - resource:
          type: topic
          name: {topic}
          patternType: literal
        operation: Read
        host: "*"
"""

group_template = """      - resource:
          type: topic
          name: {group}
          patternType: literal
        operation: Read
        host: "*"
"""

create_topic_template = """## THAIBEV-KAFKAUSER-TBV-RPTDB ##
---
apiVersion: kafka.strimzi.io/v1beta2
kind: KafkaUser
metadata:
  name: tbv-rptdb
  labels:
    strimzi.io/cluster: kafka-cluster-prd
spec:
  authentication:
    type: scram-sha-512
  authorization:
    type: simple
    acls:
      # access to kafka topic [All]
      - resource:
          type: topic
          name: bevlife-notification
          patternType: literal
        operation: All
        host: "*"
      # access to kafka group [All]
      - resource:
          type: group
          name: bevlife-group
          patternType: literal
        operation: All
        host: "*"
"""

with open(r'python\kafka\create-kafka-user\topics.txt', 'r') as file:
    # Read all lines from the file into a list
    topics = file.readlines()

topics = [topic.strip().replace(",", "") for topic in topics if topic != '\n']

output = ""

create_topic_output = ""

for topic in topics:
    # print(topic)
    output += topic_template.format(topic=topic)
    # create_topic_output += create_topic_template.format(topic=topic)

with open('add-topic.yaml', 'w') as file:
    file.write(output)

# with open('topic.yaml', 'w') as file:
#     file.write(create_topic_output)