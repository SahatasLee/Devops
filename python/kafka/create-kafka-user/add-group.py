# CREATE USER TEMPLATE

group_template = """      - resource:
          type: group
          name: {group}
          patternType: literal
        operation: All
        host: "*"
"""

with open(r'python\kafka\create-kafka-user\groups.txt', 'r') as file:
    # Read all lines from the file into a list
    groups = file.readlines()

groups = [group.strip().replace(",", "") for group in groups if group != '\n']

output = ""

for group in groups:
    # print(topic)
    output += group_template.format(group=group)
    # create_topic_output += create_topic_template.format(topic=topic)

with open(r'python\kafka\create-kafka-user\add-group.yaml', 'w') as file:
    file.write(output)

# with open('topic.yaml', 'w') as file:
#     file.write(create_topic_output)