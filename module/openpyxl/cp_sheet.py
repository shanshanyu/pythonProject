'''
create_time: 2023/6/7 16:58
author: yss
version: 1.0
'''

#把 test1.xlsx 工作簿中的 汇总表复制到 test2.xlsx 中

from openpyxl import load_workbook,Workbook

def copy_sheet(new_ws,old_ws):

    #复制sheet
    for row in old_ws.iter_rows():
        for cell in row:
            target_cell = new_ws.cell(row=cell.row,column=cell.column,value=cell.value)
            target_cell._style = cell._style




old_wb = load_workbook('test1.xlsx')
new_wb = Workbook()

new_ws = new_wb.active

old_ws = old_wb['汇总']

copy_sheet(new_ws,old_ws)


for row in new_ws.iter_rows():
    for cell in row:
        print(cell.value)

print(new_wb.sheetnames)
new_wb.save('test3.xlsx')