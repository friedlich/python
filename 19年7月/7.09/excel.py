import openpyxl  # 酱酱的注释，看仔细喽，这是一个函数库openpyxl ，用pip install安装
import re


def Exceldivide(file_dir):
    wb = openpyxl.load_workbook(file_dir)  # 打开原有的excel表
    sheet = wb.get_sheet_by_name('Sheet1')
    tuple(sheet['A1':'C3'])

    wb.create_sheet('Sheet2')  # 新建一个表
    sheet2 = wb.get_sheet_by_name('Sheet2')
    tuple(sheet2['A1':'C3'])

    L1 = re.compile(r'\d\d/\d\d/\d\d\d\d')  # 日期格式
    L2 = re.compile(r'[a-zA-Z0-9_]+@[a-zA-Z0-9-]+.com')  # 邮件格式
    l1 = []
    l2 = []
    for rows in sheet['A1':'C3']:  # 提取日期和邮件数据
        for cell in rows:
            A = L1.search(cell.value)
            a = A.group()
            B = L2.search(cell.value)
            try:
                b = B.group()
            except AttributeError:
                pass

    for rows in sheet2['A1':'A9']:  # 把日期数据写入新表
        for cell in rows:
            cell.value = a
            print(cell.coordinate, cell.value)
    for rows in sheet2['B1':'B9']:  # 把邮件数据写入新表
        for cell in rows:
            cell.value = b
            print(cell.coordinate, cell.value)
    return wb


g = Exceldivide(r'c:\Users\asus\Desktop\Python\风变Python爬虫精进\爬虫阶段练习\19年7月\7.09\source.xlsx')
g.save(r'c:\Users\asus\Desktop\Python\风变Python爬虫精进\爬虫阶段练习\19年7月\7.09\11_copy.xlsx')  # 保存