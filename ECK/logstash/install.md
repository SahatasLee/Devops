# Logstash

logstash version 8.11

https://agralrst.medium.com/how-i-send-kibana-alert-to-email-using-logstash-859c37b61d98

## RPM (Linux)

installing logstash [link](https://www.elastic.co/guide/en/logstash/current/installing-logstash.html)

Directory layout [link](https://www.elastic.co/guide/en/logstash/8.11/dir-layout.html)

Default `logstash.conf` location

```bash
/etc/logstash/conf.d/*.conf
```

config `logstash.conf`

```bash
vi /etc/logstash/conf.d/logstash.conf
```

test

```bash
cd /usr/share/logstash/
bin/logstash -e 'input { stdin { } } output { stdout {} }'
```

typing

```bash
hello world
```

run

```bash
cd /usr/share/logstash/
./bin/logstash -f config/logstash.conf

# install by RPM
cd /usr/share/logstash/
./bin/logstash -f /etc/logstash/conf.d/logstash.conf
```

### Logs

### Check ca.crt for update

### Gmail

## Kubernetes

https://github.com/elastic/helm-charts/blob/main/logstash/README.md