'''
create_time: 2023/5/30 19:52
author: yss
version: 1.0
'''

#统计字符串中出现指定字符的次数

def get_count(s,ch):
    count = 0
    #字符串是一个序列，也可以通过遍历字符串的方式实现
    count += s.count(ch.lower())
    count += s.count(ch.upper())
    return count


a = 'hello worHld'
count = a.count('ll')
print(count)

#序列解包
c = 'ab'
d,e = c  #字符串的序列解包
print(d,e)

if __name__ == '__main__':
    print(get_count(a,'h'))


