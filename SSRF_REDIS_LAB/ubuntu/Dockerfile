FROM ubuntu:18.04

RUN apt-get update

RUN apt install -y locales
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
ENV DEBIAN_FRONTEND noninteractive

RUN apt install -y php php-curl build-essential wget openssh-server cron rsyslog

RUN wget -c http://download.redis.io/redis-stable.tar.gz && \
tar -xvzf redis-stable.tar.gz && \
cd redis-stable && \
make  && \
make install

RUN mkdir /etc/redis && cp /redis-stable/redis.conf /etc/redis

COPY ./start.sh /
RUN chmod +x /start.sh

ADD ./www /www
WORKDIR /www

EXPOSE 8080
EXPOSE 22

ENTRYPOINT ["/start.sh"]
