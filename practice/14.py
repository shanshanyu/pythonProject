'''
create_time: 2023/5/31 09:20
author: yss
version: 1.0
'''

from prettytable import PrettyTable

tb = PrettyTable()
tb.field_names = ['行号','座位1','座位2','座位3','座位4','座位5']
tb_lst = [['第一行','有票','有票','有票','有票','有票'],['第二行','有票','有票','有票','有票','有票'],
          ['第三行','有票','有票','有票','有票','有票'],['第四行','有票','有票','有票','有票','有票'],
          ['第五行','有票','有票','有票','有票','有票'],['第六行','有票','有票','有票','有票','有票'],
          ['第七行','有票','有票','有票','有票','有票'],['第八行','有票','有票','有票','有票','有票']]

tb.add_rows(tb_lst) #一次性添加多行   add_rows
print(tb)

choice = input('请输入选择的座位，如 3,5表示第3排5号座位：')
x,y = choice.split(',')
x = int(x)
y = int(y)
print(x,y)

tb_lst[x-1][y] = '已售'

tb.clear_rows()  #清空所有行，但是保留 field_names（字段名）

tb.add_rows(tb_lst)
print(tb)


#打印一个多少行的表哥
def show_ticket(row_num):
    tb = PrettyTable()
    tb.field_names = ['行号','座位1','座位2','座位3','座位4','座位5']
    for i in range(row_num):
        lst = [f'第{i+1}行','有票','有票','有票','有票','有票']  #初始化一行
        tb.add_row(lst)
    print(tb)

if __name__ == '__main__':
    show_ticket(13)


