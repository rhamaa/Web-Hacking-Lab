#!/bin/bash

gosu redis redis-server --daemonize yes

python /app/www/app.py
