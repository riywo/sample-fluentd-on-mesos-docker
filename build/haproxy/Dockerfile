FROM base

MAINTAINER riywo "https://github.com/riywo"

RUN apt-get update
RUN apt-get install -y haproxy python

ADD haproxy_config.py /usr/local/bin/haproxy_config
RUN chmod +x /usr/local/bin/haproxy_config

ADD run.sh /usr/local/bin/run
RUN chmod +x /usr/local/bin/run

EXPOSE 8080
CMD ["/usr/local/bin/run", "8080"]
