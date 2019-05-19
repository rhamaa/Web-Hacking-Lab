FROM centos:7


RUN yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm -y && \
yum install http://rpms.remirepo.net/enterprise/remi-release-7.rpm -y && \
yum install yum-utils -y && \
yum-config-manager --enable remi-php73 -y

RUN yum install php php-curl wget cronie openssh-server -y && \ 
yum groupinstall "Development Tools" -y

RUN wget http://download.redis.io/releases/redis-5.0.5.tar.gz && \
tar xzf redis-5.0.5.tar.gz && \
cd redis-5.0.5 && \
make && make install

RUN mkdir /etc/redis && cp /redis-5.0.5/redis.conf /etc/redis

COPY ./start.sh /
RUN chmod +x /start.sh
ADD ./www /www
WORKDIR /www

EXPOSE 8080
EXPOSE 22

ENTRYPOINT ["/start.sh"]
