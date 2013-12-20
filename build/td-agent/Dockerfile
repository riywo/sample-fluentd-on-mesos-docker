FROM base

MAINTAINER riywo "https://github.com/riywo"

RUN echo "deb http://packages.treasure-data.com/precise/ precise contrib" > /etc/apt/sources.list.d/treasure-data.list
RUN apt-get update
RUN apt-get install -y --force-yes td-agent
RUN /etc/init.d/td-agent stop
RUN cat /dev/null > /var/log/td-agent/td-agent.log

RUN /usr/lib/fluent/ruby/bin/fluent-gem install fluent-plugin-elasticsearch

ADD run.sh /usr/local/bin/run
RUN chmod +x /usr/local/bin/run

EXPOSE 8888
CMD ["/usr/local/bin/run"]
