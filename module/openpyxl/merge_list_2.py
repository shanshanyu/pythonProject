# 2023/6/6 20:39
from openpyxl import load_workbook

wb = load_workbook('test.xlsx')


#创建新的sheet，name=merge
new_ws = wb.create_sheet('merge',index=0)

for ws in wb.worksheets:  #遍历工作簿
    row_lst = [] #获取符合条件的所有行
    if ws.title != '汇总' and ws.title != '汇总new':
        select_row = ws['A']
        #print(select_row,type(select_row)) #获取指定列  一列的值是元组，每个元组对象是一个 cell

        for cell in select_row:
            if cell.value == '核心指标':
                #row_lst.append(cell.row) #获取符合条件的行
                #print(cell.row,type(cell.row))

                # 如果这个行是一个合并的行，把所有合并的行都复制了
                for item in ws.merged_cells:
                    #print(item,type(item))
                    #print(cell.coordinate)
                    if cell.coordinate in str(item):
                        print(item)


        #for row in row_lst:
        #    new_ws.append(ws[row])