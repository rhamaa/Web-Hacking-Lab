#!/bin/bash

gosu redis redis-server

python /app/www/app.py
