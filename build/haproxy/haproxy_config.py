#!/usr/bin/python
import sys
import json
import urllib2

class MarathonHAProxyConfig(object):
    def __init__(self):
        argv = sys.argv[1:]
        if len(argv) != 4:
            print '''
            Usage: haproxy_config MARATHON_URL APP_ID HEALTH_PATH PORT
            '''.strip()
            sys.exit(1)

        self.marathon_url = argv[0]
        self.app_id       = argv[1]
        self.health_path  = argv[2]
        self.port         = argv[3]

    def run(self):
        print self.app_config()
        print self.servers_config()

    def app_config(self):
        return '''
global
  daemon
  log 127.0.0.1 local0
  log 127.0.0.1 local1 notice
  maxconn 4096

defaults
  log         global
  retries     3
  maxconn     2000
  contimeout  5000
  clitimeout  50000
  srvtimeout  50000

listen %s
  bind 0.0.0.0:%s
  mode http
  option tcplog
  option httpchk GET %s
  balance leastconn
        '''.strip() % (self.app_id, self.port, self.health_path)

    def servers_config(self):
        servers = ""
        for instance in self.instances():
            servers += "  server %s %s:%s check\n" % (instance['id'], instance['host'], instance['ports'][0])
        return servers

    def instances(self):
        return json.load(urllib2.urlopen(self.endpoints_url()))['instances']

    def endpoints_url(self):
        return self.marathon_url + '/v1/endpoints/' + self.app_id

if __name__ == '__main__':
    MarathonHAProxyConfig().run()
