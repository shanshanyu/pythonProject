# 2024/2/23  15:04

def get_log():
    #创建目标文件
    dest_file = open('/tmp/2305.log','w')
    flag = False
    with open('xx','r') as f:
        while True:
            data = f.readline()
            if '240223  4:30' in data:
                flag = True
            if flag:
                dest_file.write(data)
            if '240223  5:30' in data:
                break
    dest_file.close()





if __name__ == '__main__':
    get_log()