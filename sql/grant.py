# SQL Script
user_names = [
    '70000185',
    '70017518',
    'c1001592',
    'deusr',
    'datateam',
    '11022987',
    
               ]

# Initialize the script
script_template = """
# {user}
GRANT Alter ON dw_log.* TO '{user}'@'%';
GRANT Create ON dw_log.* TO '{user}'@'%';
GRANT Create view ON dw_log.* TO '{user}'@'%';
GRANT Delete ON dw_log.* TO '{user}'@'%';
GRANT Drop ON dw_log.* TO '{user}'@'%';
GRANT Grant option ON dw_log.* TO '{user}'@'%';
GRANT Index ON dw_log.* TO '{user}'@'%';
GRANT Insert ON dw_log.* TO '{user}'@'%';
GRANT References ON dw_log.* TO '{user}'@'%';
GRANT Select ON dw_log.* TO '{user}'@'%';
GRANT Show view ON dw_log.* TO '{user}'@'%';
GRANT Trigger ON dw_log.* TO '{user}'@'%';
GRANT Update ON dw_log.* TO '{user}'@'%';
GRANT Alter routine ON dw_log.* TO '{user}'@'%';
GRANT Create routine ON dw_log.* TO '{user}'@'%';
GRANT Create temporary tables ON dw_log.* TO '{user}'@'%';
GRANT Execute ON dw_log.* TO '{user}'@'%';
GRANT Lock tables ON dw_log.* TO '{user}'@'%';
GRANT Grant option ON dw_log.* TO '{user}'@'%';

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