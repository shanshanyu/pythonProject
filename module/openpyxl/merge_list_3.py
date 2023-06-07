'''
create_time: 2023/6/7 14:41
author: yss
version: 1.0
'''

from openpyxl import load_workbook

wb = load_workbook('test.xlsx')

#创建新的工作表
new_ws = wb.create_sheet('merge',index=0)



#复制表头
for row_index,row in enumerate(wb['唯品'][1:2]):
    for column_index,cell in enumerate(row):
        target_cell = new_ws.cell(row=row_index+1,column=column_index+1,value=cell.value)
        target_cell._style = cell._style

new_ws.merge_cells('A1:P1')

row_index = 3
#复制'核心指标'所在的行
for source_sheet in wb.worksheets:
    row_lst = []
    if source_sheet.title == '汇总':
        continue

    for row in source_sheet.iter_rows(min_row=3):
        #print(row[0].value)
        if row[0].value == '核心指标':
            row_lst.append(row[0].row)

            for merge_range in source_sheet.merged_cells:
                if row[0].coordinate in merge_range:
                    for i in range(merge_range.min_row+1,merge_range.max_row+1):
                        row_lst.append(i)




    #把 row_lst 中的行复制到 new_ws 的sheet 中
    '''
    这种方式不行，只复制了值，还需要复制格式
    for row_index in row_lst:
        new_ws.append([cell.value for cell in source_sheet[row_index]])
    '''

    #复制row_lst 中的行
    for index in row_lst:
        for cell in source_sheet[index]:
            target_cell = new_ws.cell(row=row_index,column=cell.column,value=cell.value)
            target_cell._style = cell._style
        row_index += 1

#添加合计
print(row_index)
new_ws.insert_rows(row_index)



wb.save('test1.xlsx')