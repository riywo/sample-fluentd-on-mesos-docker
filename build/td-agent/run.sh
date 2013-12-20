#!/bin/bash

cat << EOF > /etc/td-agent/td-agent.conf
<source>
  type http
  port 8888
  body_size_limit 32m
  keepalive_timeout 10s
</source>

<match **>
  type elasticsearch
  logstash_format true
  index_name fluentd
  type_name fluentd
  flush_interval 3 # For testing
  host $ES_HOST
  port $ES_PORT
</match>
EOF

/etc/init.d/td-agent start
tail -n 10000 -f /var/log/td-agent/td-agent.log
