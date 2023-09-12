# K3s

<https://docs.k3s.io/>

## Setup K3s

1. Setup DB

```bash
sudo apt install postgresql -y
```

```bash
psql --version
psql (PostgreSQL) 12.4 (Ubuntu 12.4-0ubuntu0.20.04.1)
sudo sh -c 'echo "bGlzdGVuX2FkZHJlc3NlcyA9ICcqJwo=" | base64 -d >> /etc/postgresql/12/main/postgresql.conf'
sudo sh -c 'echo "host all all 127.0.0.1/32 md5" >> /etc/postgresql/12/main/pg_hba.conf'
sudo systemctl restart postgresql
```

> psql v12.x.x change path along version if v13.x.x change to 13

```bash
/etc/postgresql/12/main/postgresql.conf
/etc/postgresql/12/main/pg_hba.conf
```

> Update

```bash
/etc/postgresql/13/main/postgresql.conf
/etc/postgresql/13/main/pg_hba.conf
```

2. create user, database and grant all privilages to user

```bash
sudo -u postgres psql -c "CREATE USER k3s PASSWORD 'k3s';"
sudo -u postgres psql -c "CREATE DATABASE k3s;"
sudo -u postgres psql -c "grant all privileges on database k3s to postgres;"
```

output

```bash
root@k3smaster:~# sudo -u postgres psql -c "CREATE DATABASE k3s;"
could not change directory to "/root": Permission denied
CREATE DATABASE
```

> Note: above is normal error
> 
> Note: fixed by below and run command

```bash
cd ~postgres
```

## Install k3s

On Master

```bash
curl -H 'Cache-Control: no-cache' -sfL https://get.k3s.io | K3S_KUBECONFIG_MODE=664 K3S_TOKEN=1234567890 sh -s - server --cluster-init --datastore-endpoint postgres://k3s:k3s@localhost:5432/k3s
```

```bash
curl -sfL https://get.k3s.io | sh -s - server \
  --token=SECRET \
  --datastore-endpoint="mysql://username:password@tcp(hostname:3306)/database-name"
  --tls-san=<FIXED_IP> # Optional, needed if using a fixed registration address
```

On Slave

```bash
curl -H 'Cache-Control: no-cache' -sfL https://get.k3s.io | K3S_KUBECONFIG_MODE=664 K3S_TOKEN=1234567890 K3S_URL=https://10.111.0.116:6443 sh -
```

## Install longhorn

```bash
wget https://raw.githubusercontent.com/longhorn/longhorn/master/deploy/longhorn.yaml

sudo apt install open-iscsi

kubectl patch storageclass longhorn -p '{"metadata":{"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'
```

## Test longhorn

```bash
wget https://raw.githubusercontent.com/longhorn/longhorn/master/examples/pod_with_pvc.yaml
kubectl apply -f pod_with_pvc.yaml
kubectl get all
```

## Uninstall longhorn
kubectl apply -f
https://raw.githubusercontent.com/longhorn/longhorn/master/uninstall/uninstall.yaml

## Install Gitlab

```bash
helm repo add gitlab https://charts.gitlab.io/
helm repo update
helm install gitlab gitlab/gitlab \
--set nginx-ingress.enabled=false \
--set global.ingress.class=traefik \
--set certmanager.install=false \
--set global.ingress.configureCertmanager=false \
--set certmanager-issuer.email=dev@example.com \
--set global.tls.enabled=false \
--set global.edition=ce \
--set global.hosts.domain=host.com \
--set global.host.gitlab.name=git.host.com \
--set global.host.registry.name=registry.host.com \
--set global.host.minio.name=minio.host.com \
--set backups.objectStorage.config.secret=secret \
--set global.time_zone=Asia/Bangkok \
--set gitlab-runner.install=false \
--set global.ingress.annotations."kubernetes\.io/ingress\.provider"=traefik \
--set gitlab.gitlab-shell.service.type=LoadBalancer \
--set global.shell.port=2222 \
--set tcp.22="gitlab/gitlab-gitlab-shell:2222" \
--namespace gitlab
```