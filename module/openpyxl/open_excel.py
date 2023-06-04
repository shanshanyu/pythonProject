'''
create_time: 2023/6/2 21:30
author: yss
version: 1.0
'''

from openpyxl import load_workbook
wb = load_workbook('test.xlsx')
print(wb,type(wb))  #<openpyxl.workbook.workbook.Workbook object at 0x7f8660d93c18> <class 'openpyxl.workbook.workbook.Workbook'>

ws = wb.active  #获取第一张工作表对象
#ws = wb['Sheet']
print(ws,type(ws))  #<Worksheet "Sheet"> <class 'openpyxl.worksheet.worksheet.Worksheet'>

for i in ws.values:
    print(i)


print(wb.sheetnames)  #返回所有sheet 的名字，为列表，列表元素为 字符串

print(wb.worksheets)  #获取所有的sheet 表对象  列表，列表元素是 sheet 对象


