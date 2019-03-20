#!/bin/bash
service apache2 start
/usr/lib/sendmail -bD -X /proc/self/fd/1
