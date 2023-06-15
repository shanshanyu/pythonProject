'''
create_time: 2023/6/9 09:16
author: yss
version: 1.0
'''

#复制 student.xlsx 中的 sheet 到新的工作簿，名字用 test_copy.xlsx

from openpyxl import load_workbook,Workbook

new_wb = Workbook()
new_ws = new_wb.active

old_wb = load_workbook('student.xlsx')
old_ws = old_wb.active

#遍历 old_ws 中的所有行，复制到 new_ws 中,只能复制一个工作表

'''for row in old_ws.iter_rows():
    for cell in row:
        new_ws.cell(row=cell.row,column=cell.column,value=cell.value)
'''
row_lst = []
for worksheet in old_wb.worksheets: #遍历工作簿
    for row in worksheet.iter_rows(): #遍历工作表
        tmp_row = []   #方法一
        for cell in row:
            tmp_row.append(cell.value)
        row_lst.append(tmp_row)
        '''   #方法二
        tmp_row = [cell.value for cell in row]  #遍历行  #
        row_lst.append(tmp_row)
        '''
for row in row_lst:
    new_ws.append(row)



new_wb.save('test_copy.xlsx')