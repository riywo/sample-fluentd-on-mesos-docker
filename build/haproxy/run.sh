#!/bin/bash

PORT=$1
/usr/local/bin/haproxy_config $MARATHON_URL $APP_ID $HEALTH_PATH $PORT > /etc/haproxy/haproxy.cfg

/usr/sbin/haproxy -f /etc/haproxy/haproxy.cfg -d
