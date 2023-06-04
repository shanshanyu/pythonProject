'''
create_time: 2023/6/4 08:00
author: yss
version: 1.0
'''

#查看合并的单元格列表

from openpyxl import load_workbook

wb = load_workbook('test.xlsx')

#print(type(wb))

ws = wb.worksheets[1]
#print(type(ws))

wm = ws.merged_cells
print(wm,type(wm))
