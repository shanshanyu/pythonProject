'''
create_time: 2023/6/2 22:04
author: yss
version: 1.0
'''
from openpyxl import load_workbook


wb = load_workbook('test.xlsx')

all_sheetname = wb.sheetnames  #获取所有的工作表名
all_sheet = wb.worksheets  #获取所有的工作表对象
print(all_sheet,type(all_sheet))

#new_sheet = wb.create_sheet('merge') #默认在最后创建一个sheet
new_sheet = wb.create_sheet('merge',index=0)  #在 index为0的位置创建一个sheet

for sheet in all_sheet[1:]:  #遍历工作表
    print(sheet,type(sheet))
    for row in sheet.iter_rows(min_row=2):
        if row[0].value == '核心指标':
            new_row = [cell.value for cell in row]
            new_sheet.append(new_row)

wb.save('test.xlsx')  #工作簿保存