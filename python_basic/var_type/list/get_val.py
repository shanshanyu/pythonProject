'''
create_time: 2024/3/7 14:16
author: yss
desc: 获取列表中最大和第二大的值
version: 1.0

现获取最大的值->把剩下的值组成列表，再取最大
'''

a = [1,9,3,10,5,6]

def main():
    max_val = max(a)
    a.remove(max_val)
    second_max = max(a)
    return max_val,second_max

if __name__ == '__main__':
    b,c = main()
    print(b,c)
