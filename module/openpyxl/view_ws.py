'''
create_time: 2023/6/2 22:27
author: yss
version: 1.0
'''
from openpyxl import load_workbook

wb = load_workbook('student.xlsx')

ws = wb.active  #获取第一个sheet

print(ws.values,type(ws.values))  #<generator object Worksheet.values at 0x7fea48a25b10> <class 'generator'>
for i in ws.values:
    print(i,type(i))  #遍历后每个元素是一个元组，元组里面的元素是值


ws_val_lst = list(ws.values)
print(ws_val_lst,type(ws_val_lst))  #generateor 对象可以转换成列表

print('-'*100)
print(ws.rows,type(ws.rows))
for i in ws.rows:  #<generator object Worksheet._cells_by_row at 0x7f8d48dbcb10> <class 'generator'>
    print(i,type(i)) #遍历后每个元素是一个元组，元组里面的元素是一个 cell

row_lst = ws.iter_rows()
print(row_lst,type(row_lst))





