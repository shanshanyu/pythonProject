# 2023/5/28  20:58
#向文件中输出一些内容
with open('test.txt','w',buffering=True,encoding='utf-8') as file: #文本模式 io 需要带缓冲,二进制模式不需要encoding
    #ValueError: can't have unbuffered text I/O
    #ValueError: binary mode doesn't take an encoding argument
    file.write('小玉米好样的!'+'\n')
    print('小玉米好样的！！', file=file)  #print也可以向文件中输出消息

