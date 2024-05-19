# Installed by helm

https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack

## List versions
```bash
helm search repo prometheus-community/kube-prometheus-stack --versions
```

## Install
```bash
helm -n prometheus install <release-name> prometheus-community/kube-prometheus-stack
```

## Default User
```bash
$ kubectl get secret --namespace prometheus prometheus-grafana  -o jsonpath="{.data.admin-user}" | base64 --decode ; echo
$ admin
```

## Default Password
```bash
$ kubectl get secret --namespace prometheus prometheus-grafana  -o jsonpath="{.data.admin-password}" | base64 --decode ; echo
$ prom-operator
```

## Set
```bash
helm -n prometheus install <release-name> prometheus-community/kube-prometheus-stack --set 
```

## Config Grafana.ini

```bash
## Grafana's primary configuration
## NOTE: values in map will be converted to ini format
## ref: http://docs.grafana.org/installation/configuration/
```
