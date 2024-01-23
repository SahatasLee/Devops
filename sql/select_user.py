# SQL Script
user_names = [
                
               ]

# Initialize the script
script_template = """
# {user}
GRANT Select ON RTM_Staging.* TO '{user}'@'%';
"""

# Initialize an empty result script
result_script = ""

for name in user_names:
    print(name)
    result_script += script_template.format(user=name)

# Save the modified script to a file
with open('tidb_select_script.sql', 'w') as file:
    file.write(result_script)

print("Script saved to script.sql")