# Change Password
script_template = '''
# {user}
ALTER USER '{user}'@'%' IDENTIFIED BY '{password}';
'''

uat_list = []
with open(r"C:\Users\sahatas.l\Documents\users_uat.txt", 'r') as file:
    username = ''
    for line in file:
        # Split the line into username and password using ":" as a delimiter
        parts = line.strip().split(':')
        if len(parts) == 2:
            
            if parts[0] == 'Username':
                # username = parts[1].strip()
                uat_list += [parts[1].strip()]
            elif parts[0] == 'Password':
                pass
            else:
                print("Error values:", parts)

print(uat_list)

credentials_dict = {}

prd_list = []

# Open the text file for reading
with open(r"C:\Users\sahatas.l\Documents\users_prd.txt", 'r') as file:
    # Read each line in the file
    username = ''
    for line in file:
        # Split the line into username and password using ":" as a delimiter
        parts = line.strip().split(':')
        if len(parts) == 2:
            
            if parts[0] == 'Username':
                prd_list.append(parts[1].strip())
                if parts[1].strip() not in uat_list:
                    print("Not Match:", parts[1].strip())
                    continue
                username = parts[1].strip()
            elif parts[0] == 'Password' and username in uat_list:
                password = parts[1]
                credentials_dict[username] = password.strip()
            else:
                print("Error values:", parts)

# print(credentials_dict)
for i in credentials_dict:
    print(i, credentials_dict[i])

for user in uat_list:
    if user not in prd_list:
        print("User {user} not in prd_list".format(user=user))

# Initialize an empty result script
result_script = ""

# 
for user in credentials_dict:
    result_script += script_template.format(user=user, password=credentials_dict[user])

# Save the modified script to a file
with open('tidb_change_password_script.sql', 'w') as file:
    file.write(result_script)

print("Script saved to script.sql")
