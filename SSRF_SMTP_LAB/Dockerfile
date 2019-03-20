FROM ubuntu:latest

MAINTAINER Ilya Isaev "me@ilyaisaev.com"

WORKDIR /etc/mail

RUN apt-get update

RUN apt install -y locales
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
ENV DEBIAN_FRONTEND noninteractive


RUN set -e && apt-get install -y sendmail

RUN apt install -y apache2 php libapache2-mod-php php-curl

# PHP
COPY src/curl.php /var/www/html
COPY src/index.html /var/www/html

RUN chmod -R 555 /var/www/html/

# Sendmail
COPY sendmail.mc /etc/mail/sendmail.mc
RUN m4 sendmail.mc > sendmail.cf && \
 echo "Connect:172 RELAY" >> access && \
 echo "Connect:10 RELAY" >> access && \
 make

EXPOSE 25
EXPOSE 80

COPY src/start.sh /start.sh
RUN chmod 555 /start.sh

ENTRYPOINT [ "/start.sh" ]
