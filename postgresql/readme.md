# Postgresql

## Install by Helm

```bash
helm install psql bitnami/postgresql --namespace psql --create-namespace --set global.storageClass=nfs-client
```

Output:

```bash
root@node1:~# helm install psql bitnami/postgresql --namespace psql --create-namespace --set global.storageClass=nfs-client --version 12.0.0
NAME: psql
LAST DEPLOYED: Tue Sep  5 14:49:56 2023
NAMESPACE: psql
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
CHART NAME: postgresql
CHART VERSION: 12.0.0
APP VERSION: 15.0.0

** Please be patient while the chart is being deployed **

PostgreSQL can be accessed via port 5432 on the following DNS names from within your cluster:

    psql-postgresql.psql.svc.cluster.local - Read/Write connection

To get the password for "postgres" run:

    export POSTGRES_PASSWORD=$(kubectl get secret --namespace psql psql-postgresql -o jsonpath="{.data.postgres-password}" | base64 -d)

To connect to your database run the following command:

    kubectl run psql-postgresql-client --rm --tty -i --restart='Never' --namespace psql --image docker.io/bitnami/postgresql:15.0.0-debian-11-r1 --env="PGPASSWORD=$POSTGRES_PASSWORD" \
      --command -- psql --host psql-postgresql -U postgres -d postgres -p 5432

    > NOTE: If you access the container using bash, make sure that you execute "/opt/bitnami/scripts/postgresql/entrypoint.sh /bin/bash" in order to avoid the error "psql: local user with ID 1001} does not exist"

To connect to your database from outside the cluster execute the following commands:

    kubectl port-forward --namespace psql svc/psql-postgresql 5432:5432 &
    PGPASSWORD="$POSTGRES_PASSWORD" psql --host 127.0.0.1 -U postgres -d postgres -p 5432

```