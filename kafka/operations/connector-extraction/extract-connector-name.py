import re

# Read text from input.txt file
with open(r"C:\Users\sahatas.l\Devops\kafka\operations\connector-extraction\input.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Define regex pattern for the connector label
connector_pattern = r"connector\s*=\s*(.*)"

# Search for the connector pattern in the text
matches = re.findall(connector_pattern, text)

# Extract the value associated with the connector label
if matches:
    print("Connector values:")
    num=0
    for match in matches:
        print(match)
        num+=1
        # Write the connector value to a text file
        with open(r"C:\Users\sahatas.l\Devops\kafka\operations\connector-extraction\output.txt", "a", encoding="utf-8") as file:
            file.write(match + "\n")  # Add a newline after each match
    print(f"{num} Connector values have been written to output.txt")
else:
    print("Connector not found in the text.")