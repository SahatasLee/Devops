# create TOPICS

template = """      - resource:
          type: topic
          name: {topic}
          patternType: literal
        operation: All
        host: "*"
"""

with open('topics.txt', 'r') as file:
    # Read all lines from the file into a list
    topics = file.readlines()

topics = [topic.strip() for topic in topics if topic != '\n']

output = ""

for topic in topics:
    # print(topic)
    output += template.format(topic=topic)

with open('topics.yaml', 'w') as file:
    file.write(output)