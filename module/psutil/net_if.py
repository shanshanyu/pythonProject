'''
create_time: 2023/6/14 10:31
author: yss
version: 1.0
'''
import psutil

#print(psutil.net_if_addrs(),type(psutil.net_if_addrs()))



for address in psutil.net_if_addrs().items():

    print(address)
    print(address[1][0].address)  #address[1][0] 是一个 snicaddr 对象，通过 .address 访问 address 属性


a = {1:'a',2:'b'}
print(a.items())
for i in a.items():
    print(i,type(i))   #字典的 items()返回一个可迭代对象，每个对象是一个元组




print(psutil.net_if_addrs())  #返回值是一个字典