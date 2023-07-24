'''
create_time:  21:44
author: yss
version: 1.0
'''
from pathlib import *
import fnmatch

pp = PurePath('set.py')
print(type(pp))
pp1 = PurePosixPath('hello.py')
print((type(pp1)))
pp2 = PurePath(pp,pp1)
print(type(pp2))
print(pp)
print(pp1)
print(pp2)

pp3 = PurePath()
print(type(pp3))
print(pp3)

pp4 = Path('../..')
for i in pp4.iterdir():
    print(i)

print("glob===")
for i in pp4.glob('*.py'):
    print(i)

print(fnmatch.translate('[a-c].py'))