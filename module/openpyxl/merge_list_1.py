'''
create_time: 2023/6/4 09:49
author: yss
version: 1.0
'''

from openpyxl import load_workbook

wb = load_workbook('test.xlsx')

def cancel_merge(ws):
    for item in ws.merged_cells:
        print(item,type(item))
        print(str(item))
        ws.unmerge_cells(range_string=str(item))

#创建新的sheet，name=merge
new_ws = wb.create_sheet('merge',index=0)
#header = wb['唯品'][1:3]  #获取工作表的 1 2 两行当做表头 ws[1:3]  获取 1 2行所有的单元格对象，返回值是一个元组嵌套元组


for sheet in wb.sheetnames:  #遍历工作簿
    row_lst = [] #获取符合条件的所有行
    if sheet != '汇总' and sheet != 'merge':
        ws = wb[sheet] #获取工作表
        select_row = ws['A']  #获取指定列  一列的值是元组，每个元组对象是一个 cell
        print(select_row,type(select_row))
        #cancel_merge(ws)
        for cell in select_row:
            if cell.value == '核心指标':
                row_lst.append(cell.row) #获取符合条件的行
                print(cell.row,type(cell.row))

        for row in row_lst:
            new_ws.append(ws[row])








'''header_lst = []
for header_row in header: 
    tmp_lst = [cell for cell in header_row]
    header_lst.append(tmp_lst)
'''

print(header,type(header))
#复制表头


wb.save('test1.xlsx')

