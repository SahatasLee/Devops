# Two Fer

    name=${1:-"you"}
    echo "One for $name, one for me."

## Let's break down how this script works:

1. **name=${1:-"you"}:**

- Here, `$1` represents the first command-line argument passed to the script.
- The syntax `${var:-default}` is used to set a default value for a variable (name in this case) if it is not provided as an argument.
- If the script is executed without any arguments (i.e., bash two_fer.sh), `$1` will be empty, and name will be set to the default value "you".
- If the script is executed with an argument (e.g., bash two_fer.sh Alice), `$1` will be set to "Alice", and name will be set to "Alice".

2. echo "One for $name, one for me.":

- The echo command is used to print the output to the terminal.
- The message being printed contains the variable name, which will either be the first command-line argument passed to the script or the default value "you" if no argument is provided.
- So, the output will be either "One for you, one for me." (if no argument is provided) or "One for Alice, one for me." (if "Alice" is provided as an argument).