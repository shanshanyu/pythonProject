# 2023/5/24 22:09
import time
cur_time = time.localtime(time.time())

str_cur_time = time.strftime('%Y%m%d-%H%M%S',cur_time)

print(str_cur_time,type(str_cur_time))

print(time.time(),type(time.time()))  #返回的是一个时间戳  是一个浮点数
print(time.localtime(),type(time.localtime()))  #返回的是一个 struct_time 对象
print(time.gmtime(),type(time.gmtime()))  #返回的是一个 struct_time 对象


