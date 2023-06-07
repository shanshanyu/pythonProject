'''
create_time: 2023/6/2 21:13
author: yss
version: 1.0
'''
from openpyxl import Workbook

wb = Workbook()   #创建工作簿
print(wb,type(wb))  #<openpyxl.workbook.workbook.Workbook object at 0x7f8fc8070668> <class 'openpyxl.workbook.workbook.Workbook'>

ws = wb.active
print(ws,type(ws))  #<Worksheet "Sheet"> <class 'openpyxl.worksheet.worksheet.Worksheet'>

ws.append(['zhangsan',15,'male'])
ws.append(['lisi',16,'female'])
ws.title = 'new_sheet'

wb.save(r'student.xlsx')  #sheet默认 1 个，名字 Sheet

