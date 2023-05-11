'''
create_time: 2023/4/19 16:35
author: yss
version: 1.0
'''
import subprocess
import sys

p = subprocess.Popen("sleep 8",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
try:
    outs, errs = p.communicate(timeout=5)
except TimeoutError:
    print("timeout",sys.stderr)
    p.kill()
    outs,errs = p.communicate()
ret = {'ret:':p.returncode,'stdout:':outs}
print(ret)



