'''
暂停一秒输出，并格式化当前时间
'''
import time


def strip_time():
    time.sleep(1)
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))  #将 struct time 转换成字符串
    print(time.time())  # 结果是浮点数
    print(time.localtime())  #struct time结构，是本地时间
    print(time.gmtime())   #struct time 结构，是utc 时间


if __name__ == '__main__':
    strip_time()