'''
create_time: 2023/5/28 21:34
author: yss
version: 1.0
'''

#输出带颜色的文字

print('\033[1;35m 图书音像勋章 \033[0m')

height = 170
weight = 68

bmi = weight/(height+weight)

#3种格式化字符串的方式
print('身高 {}'.format(height))
print(f'体重 {weight}')
print('bmi %f' % bmi)


list1 = [1,2,3,4,5]
list2 = ['张三','李四','王五','赵六','王麻子']

print(zip(list1,list2),type(zip(list1,list2)))  #zip压缩后是一个zip 对象
#遍历zip对象
for i in zip(list1,list2):
    #print(i,type(i))
    print(i[0],i[1])

for key,val in zip(list1,list2):  #序列解包，遍历 zip
    #print(i,type(i))
    print(key,val)
