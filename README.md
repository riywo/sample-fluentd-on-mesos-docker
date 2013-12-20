# Fluentd on Mesos + Docker + Marathon

This is a sample of fluentd running on mesos, docker and marathon.

## Overview

![diagram](https://cacoo.com/diagrams/9XIEXwoUNUvOOuZ2-AB7C1.png)

## Prerequire

- Vagrant 1.4.1 (I checked only this version)
- vagrant-hostmanager plugin
    - [smdahlen/vagrant-hostmanager](https://github.com/smdahlen/vagrant-hostmanager)

## Usage

### Startup boxes

    $ git clone https://github.com/riywo/sample-fluentd-on-mesos-docker
    $ cd sample-fluentd-on-mesos-docker
    $ vagrant up

### Make sure the /etc/hosts is recognized by dnsmasq

    $ vagrant ssh mesos-master
    $ sudo service lxc-net restart
    
    $ vagrant ssh mesos-slave[12]
    $ sudo service lxc-net restart

### Start containers of Elasticsearch and Kibana

    $ vagrant ssh mesos-master
    $ sudo docker run -d -p 9200:9200 arcus/elasticsearch
    $ sudo docker run -d -p 8888:80 -e ES_PORT=9200 -e ES_HOST=mesos-master arcus/kibana

### Start Fluentd(td-agent) instances via Marathon
    
    $ vagrant ssh mesos-master
    $ cat /vagrant/td-agent.json | http POST http://mesos-master:8080/v1/apps/start
    HTTP/1.1 204 No Content
    Content-Type: application/json
    Server: Jetty(8.y.z-SNAPSHOT)

### Start HAProxy container
    
    $ vagrant ssh mesos-master
    $ sudo docker run -d -p 5555:8080 -e MARATHON_URL=http://mesos-master:8080 -e APP_ID=td-agent -e HEALTH_PATH=/?json=%7B%7D haproxy
    
### Send logs!

    $ vagrant ssh mesos-master
    $ http POST http://mesos-master:5555/test a=1