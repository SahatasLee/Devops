# SQL Script
user_names = [
                'i1034253',
                '70076127',
                'i1003096', #
                'i1026445', #
                '70003867',
                'i1034834',
                'i1022635',
                'i1032554',
                'i1033139',
                '70017550',
                '70082951',
                '70092728',
                '70038535',
                '70054381',
                '70073483',
                '70086300',
                '70066871',
                '50181181', #
                '70086256',
                '70090858',
                '50378215'
               ]

# Initialize the script
script_template = """
# {user}
GRANT Select ON RPT_Inventory.* TO '{user}'@'%';
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