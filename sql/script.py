# SQL Script
table_names = [
                'RPT_Sales_Internal',
                'RPT_Sales_External',
                'RPT_Sales_ThirdParty',
                'RPT_CRM',
                'RPT_Inventory',
                'RPT_Logistics',
                'RPT_Production',
                'RPT_Marketing',
                'RPT_MasterData',
                'RPT_Procurement',
                'RPT_Survey',
                'RPT_Finance'
               ]

# Initialize the script
script_template = """
# {table}
GRANT Alter ON {table}.* TO 'datateam'@'%';
GRANT Create ON {table}.* TO 'datateam'@'%';
GRANT Create view ON {table}.* TO 'datateam'@'%';
GRANT Delete ON {table}.* TO 'datateam'@'%';
GRANT Drop ON {table}.* TO 'datateam'@'%';
GRANT Index ON {table}.* TO 'datateam'@'%';
GRANT Insert ON {table}.* TO 'datateam'@'%';
GRANT References ON {table}.* TO 'datateam'@'%';
GRANT Select ON {table}.* TO 'datateam'@'%';
GRANT Show view ON {table}.* TO 'datateam'@'%';
GRANT Trigger ON {table}.* TO 'datateam'@'%';
GRANT Update ON {table}.* TO 'datateam'@'%';
GRANT Create routine ON {table}.* TO 'datateam'@'%';
GRANT Execute ON {table}.* TO 'datateam'@'%';
GRANT Create temporary tables ON {table}.* TO 'datateam'@'%';
GRANT Alter routine ON {table}.* TO 'datateam'@'%';
"""

# Initialize an empty result script
result_script = ""

for name in table_names:
    print(name)
    result_script += script_template.format(table=name)

# Save the modified script to a file
with open('tidb_script.sql', 'w') as file:
    file.write(result_script)

print("Script saved to script.sql")