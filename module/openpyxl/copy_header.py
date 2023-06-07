# 2023/6/6 20:46
#从其他sheet 中copy 表头，包括样式也要保持一致
#从唯品中copy表头到 merge sheet 中

from openpyxl import load_workbook
from openpyxl.utils import range_boundaries

wb = load_workbook('test.xlsx')
# 遍历其他工作表（除了第一个）

ws = wb.create_sheet('merge',index=0)

old_ws = wb['唯品']

print(old_ws.merged_cells,type(old_ws.merged_cells))
# 复制头两行
for row in old_ws[1:2]:  #返回的值是元组嵌套元组，一个元组元素代表一行
    for source_cell in row: #遍历每一行
        target_cell = ws.cell(row=source_cell.row,column=source_cell.column,value=source_cell.value)
        target_cell._style = source_cell._style  #格式保持一致

for item in old_ws.merged_cells:
    print(item,type(item))
    ws.merge_cells(str(item))  #可行
        # 处理合并单元格
        #if old_ws.cell(row=source_cell.row, column=source_cell.column).coordinate in old_ws.merged_cells:
        #    merged_range = old_ws.merged_cells.remove(old_ws.cell(row=source_cell.row, column=source_cell.column).coordinate)
        #    ws.merge_cells(merged_range)

#print(wb['唯品'].merged_cells.ranges,type(wb['唯品'].merged_cells.ranges))  #返回值是一个集合
#for merge_range in old_ws.merged_cells.ranges: #是一个集合，每个元素是一个 MergedCellRange
    #print(merge_range,type(merge_range))
    #start_row,start_col,end_row,end_col = merge_range.bounds
    #ws.merge_cells(start_row=1, start_column=1, end_row=end_row - start_row + 1,end_column=end_col - start_col + 1)
    #for row in old_ws.iter_rows(min_row=start_row,max_row=end_row,min_col=start_col,max_col=end_col)


    #start_cell,end_cell = range_boundaries(merge_range)
    #print(start_cell,type(start_cell))




wb.save(r'test1.xlsx')
