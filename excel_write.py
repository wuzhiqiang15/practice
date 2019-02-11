# 创建excel文件，并且写入内容
'''
说明：
由于xlwt值支持office 2003之前的版本，所以我们这里用第三方库“openpyxl”
'''

from openpyxl.reader.excel import load_workbook
import os

filename = "data_01.xlsx"
filePath = os.path.join(os.getcwd(), filename)

wb = load_workbook(filePath)

print(wb.get_named_ranges())