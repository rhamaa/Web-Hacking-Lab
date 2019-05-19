#!/bin/bash

service cron start
service rsyslog start

redis-server /etc/redis/redis.conf --daemonize yes

php -S 0.0.0.0:8080
