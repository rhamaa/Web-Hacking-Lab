#!/bin/bash

redis-server /etc/redis/redis.conf --daemonize yes

/usr/sbin/init

/sbin/crond

php -S 0.0.0.0:8080
