CREATE USER 'less'@'%' IDENTIFIED BY '12341234';
GRANT PROCESS, CONFIG ON *.* TO 'less'@'%';
GRANT SHOW DATABASES ON *.* TO 'less'@'%';
GRANT DASHBOARD_CLIENT ON *.* TO 'less'@'%';

-- To modify the configuration items on the interface after signing in to TiDB Dashboard, the user-defined SQL user must be granted with the following privilege.
GRANT SYSTEM_VARIABLES_ADMIN ON *.* TO 'less'@'%';

-- To use the Fast Bind Executions Plan feature (https://docs.pingcap.com/tidb/v7.1/dashboard-statement-details#fast-plan-binding) on the interface after signing in to TiDB Dashboard, the user-defined SQL user must be granted with the following privileges.
GRANT SYSTEM_VARIABLES_ADMIN ON *.* TO 'less'@'%';
GRANT SUPER ON *.* TO 'less'@'%';