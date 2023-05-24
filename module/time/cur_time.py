# 2023/5/24 22:09
import time
cur_time = time.localtime(time.time())

str_cur_time = time.strftime('%Y%m%d-%H%M%S',cur_time)

print(str_cur_time,type(str_cur_time))

