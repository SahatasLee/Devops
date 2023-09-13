# Create User

```sql
CREATE USER 'sample'@'%' IDENTIFIED BY '1234';
GRANT Usage ON *.* TO 'sample'@'%';
```

replace **sample** to your username.

replace **1234** to your password.

```sql
GRANT Select ON test.* TO 'sample'@'%';
```
replace **test** to request database. In [create user file](../sql/create_user.sql) or [create admin file](../sql/create_admin_user.sql)

## run sql command

```sql
CREATE USER 'sample'@'%' IDENTIFIED BY '1234';
GRANT Usage ON *.* TO 'sample'@'%';
GRANT Select ON test.* TO 'sample'@'%';
GRANT Insert ON test.* TO 'sample'@'%';
GRANT Drop ON test.* TO 'sample'@'%';
GRANT Create ON test.* TO 'sample'@'%';
GRANT Alter ON test.* TO 'sample'@'%';
```

## full control

```sql
CREATE USER 'sample'@'%' IDENTIFIED BY '1234';
GRANT Usage ON *.* TO 'sample'@'%';
GRANT Select ON test.* TO 'sample'@'%';
GRANT Insert ON test.* TO 'sample'@'%';
GRANT Drop ON test.* TO 'sample'@'%';
GRANT Create ON test.* TO 'sample'@'%';
GRANT Alter ON test.* TO 'sample'@'%';
GRANT Create view ON test.* TO 'sample'@'%';
GRANT Delete ON test.* TO 'sample'@'%';
GRANT Grant option ON test.* TO 'sample'@'%';
GRANT Index ON test.* TO 'sample'@'%';
GRANT References ON test.* TO 'sample'@'%';
GRANT Show view ON test.* TO 'sample'@'%';
GRANT Trigger ON test.* TO 'sample'@'%';
GRANT Update ON test.* TO 'sample'@'%';
GRANT Alter routine ON test.* TO 'sample'@'%';
GRANT Create routine ON test.* TO 'sample'@'%';
GRANT Create temporary tables ON test.* TO 'sample'@'%';
GRANT Execute ON test.* TO 'sample'@'%';
GRANT Lock tables ON test.* TO 'sample'@'%';
GRANT Grant option ON test.* TO 'sample'@'%';
GRANT Create user ON *.* TO 'sample'@'%';
GRANT Event ON *.* TO 'sample'@'%';
GRANT File ON *.* TO 'sample'@'%';
GRANT Process ON *.* TO 'sample'@'%';
GRANT Reload ON *.* TO 'sample'@'%';
GRANT Replication client ON *.* TO 'sample'@'%';
GRANT Replication slave ON *.* TO 'sample'@'%';
GRANT Show databases ON *.* TO 'sample'@'%';
GRANT Shutdown ON *.* TO 'sample'@'%';
GRANT Super ON *.* TO 'sample'@'%';
GRANT Create tablespace ON *.* TO 'sample'@'%';
GRANT BACKUP_ADMIN ON *.* TO 'sample'@'%';
GRANT RESTORE_ADMIN ON *.* TO 'sample'@'%';
GRANT SYSTEM_USER ON *.* TO 'sample'@'%';
GRANT SYSTEM_VARIABLES_ADMIN ON *.* TO 'sample'@'%';
GRANT ROLE_ADMIN ON *.* TO 'sample'@'%';
GRANT CONNECTION_ADMIN ON *.* TO 'sample'@'%';
GRANT PLACEMENT_ADMIN ON *.* TO 'sample'@'%';
GRANT DASHBOARD_CLIENT ON *.* TO 'sample'@'%';
GRANT RESTRICTED_TABLES_ADMIN ON *.* TO 'sample'@'%';
GRANT RESTRICTED_STATUS_ADMIN ON *.* TO 'sample'@'%';
GRANT RESTRICTED_VARIABLES_ADMIN ON *.* TO 'sample'@'%';
GRANT RESTRICTED_USER_ADMIN ON *.* TO 'sample'@'%';
GRANT RESTRICTED_CONNECTION_ADMIN ON *.* TO 'sample'@'%';
GRANT RESTRICTED_REPLICA_WRITER_ADMIN ON *.* TO 'sample'@'%';
GRANT Grant option ON *.* TO 'sample'@'%';
```