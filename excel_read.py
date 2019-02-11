# 读取excel中的文件
import xlrd
import os
from datetime import date,datetime

# 定义excel文件的路径
filename = "data_01.xlsx"
filePath = os.path.join(os.getcwd(), filename)
print('\n', 'excel文件为：', filePath)

# 打开excel文件
x1 = xlrd.open_workbook(filePath)

print('\n=================================分割线====================================\n')

# 获取sheet对象（工作表）
print('\n', "sheet_names:", x1.sheet_names())   # 获取所有sheet名称
print('\n', "sheet_number:", x1.nsheets)       # 获取sheet数量
print('\n', "sheet_object:", x1.sheets)        # 获取所有sheet里面的内容
print('\n',"By_name:", x1.sheet_by_name("Sheet—1"))   # 通过sheet名查找
print('\n',"By_index:", x1.sheet_by_index(2))        # 通过索引查找sheet
print('\n', 'Sheet-1里面的内容:', x1.sheets()[2])     # 同上，索引查找的另一种方式

print('\n=================================分割线====================================\n')

# 获取sheet的汇总数据
sheet1 = x1.sheet_by_name("Sheet—1")

print("sheet name:", sheet1.name)  # 获取sheet的名称
print("row_num:", sheet1.nrows)    # 获取该sheet的 行数
print("col_num:", sheet1.ncols)    # 获取该sheet的 列数

print('\n=================================分割线====================================\n')

# 单元格批量读取______“行”操作：
print('第一行所有的内容：', sheet1.row_values(0))     # 获取第一行的所有内容
print('第2行所有的内容：', sheet1.row_values(1))    # 获取第二行的所有内容
print(sheet1.row(0))    # 获取单元格的值类型和内容
print(sheet1.row_types(0))  # 获取单元格数据类型

print('\n=================================分割线====================================\n')

# 单元格批量读取____“列”操作
print('行信息为：',sheet1.row_values(0,1,5))   # 获取第一行，第2-5列的内容（索引从0开始，不包含第5列）
print('列信息为：',sheet1.col_values(0,0,4))   # 获取第一列，第1—4行的内容（不包括第4行）
print(sheet1.row_slice(2,0,3))    # 获取第三行，第0-3列的值类型和内容（不包括第三列）

print('\n=================================分割线====================================\n')

# 特定单元格内容的读取
print(sheet1.cell_value(1,2))   # 获取第一行，第3列的内容
print(sheet1.cell(1,2).value)   # 同上，另一种实现方式
print(sheet1.row(1)[2].value)   # 同上，另一种实现方式

# 特定单元格类型的获取
'''
数据类型：
空：0 、 字符串：1 、 数字：2 、 日期：3 、 Bool：4  、 Error：5
'''
print(sheet1.cell_type(1, 2))   # 获取第一行，第3列的类型
