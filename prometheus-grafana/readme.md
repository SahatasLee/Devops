# Prometheus

Install app

Installed by [helm](\helm.md)

## Install prometheus

https://www.cherryservers.com/blog/install-prometheus-ubuntu

```bash
wget https://github.com/prometheus/prometheus/releases/download/v2.45.0/prometheus-2.45.0.linux-amd64.tar.gz
tar xvfz prometheus-*.tar.gz
cd prometheus-*
./prometheus --config.file=prometheus.yml
```

## Install node exporter

https://developer.couchbase.com/tutorial-node-exporter-setup

```bash
wget https://github.com/prometheus/node_exporter/releases/download/v1.6.1/node_exporter-1.6.1.linux-amd64.tar.gz
tar -xzvf node_exporter-*.*.tar.gz
cd node_exporter-*.*
./node_exporter --web.listen-address 127.0.0.1:8080
```

## Install Grafana

https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-grafana-on-ubuntu-22-04

## Uninstall Grafana

```bash
systemctl stop grafana-server
systemctl disable grafana-server
apt unintall grafana-server
```

## Create Dashboard Grafana