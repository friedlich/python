#Excel读取的代码：

import openpyxl
wb = openpyxl.load_workbook(r'c:/Users/asus/Desktop/Python/风变Python爬虫精进/爬虫阶段练习/6.19/Jay1.xlsx')
sheet = wb['song_list']
sheetname = wb.sheetnames
print(sheetname)
A1_value = sheet['A1'].value
print(A1_value)