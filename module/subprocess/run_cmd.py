'''
create_time: 2023/3/29 17:16
author: yss
version: 1.0
'''
import subprocess
def run_cmd(cmd):
    p = subprocess.Popen(cmd,shell=True,universal_newlines=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    stdout,stderr = p.communicate()
    res = {'returncode:': p.returncode,'stdout:':p.stdout,'stderr:': p.stderr}
    return res

res = run_cmd("ls -l")
print(res)