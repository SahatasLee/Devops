# Config

## Path

```bash
# linux path
vi /etc/logstash/conf.d/logstash.conf

# ruby file
vi /etc/logstash/apm-alert.rb

# Run by full path
/usr/share/logstash/bin/logstash -f /etc/logstash/conf.d/logstash.conf

# setting
/usr/share/logstash/bin/logstash --path.settings /etc/logstash --path.logs /var/log/logstash

# gem install libralies

```

## Elasticsearch filter plugin
https://www.elastic.co/guide/en/logstash/current/plugins-inputs-elasticsearch.html#plugins-inputs-elasticsearch-size

## Ruby Plugin