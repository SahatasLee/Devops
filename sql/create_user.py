import secrets
import string

# SQL Script
user_names = [
                
               ]

# Initialize the script
script_template = """
# {user}
CREATE USER '{user}'@'%' IDENTIFIED BY '{password}';
"""

txt_template = """
Username: {user}
Password: {password}
"""

# Initialize an empty result script
result_script = ""
result_txt = ""

# Random password
def random_password():
    # Define the length of the password
    password_length = 8  # You can adjust this to your desired length

    # Define characters to use for generating the password
    password_characters = string.ascii_letters + string.digits # + string.punctuation

    # Generate a random password
    random_password = ''.join(secrets.choice(password_characters) for i in range(password_length))

    print("Random Password:", random_password)
    return random_password

for name in user_names:
    print(name)
    password=random_password()
    result_script += script_template.format(user=name, password=password)
    result_txt += txt_template.format(user=name, password=password)

# Save the modified script to a file
with open('tidb_create_users_script.sql', 'w') as file:
    file.write(result_script)

with open(r'C:\Users\sahatas.l\Documents\users.txt', 'w') as file:
    file.write(result_txt)

print("Script saved to script.sql")