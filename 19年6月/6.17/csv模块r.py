import csv
csv_file = open(r'c:/Users/asus/Desktop/Python/风变Python爬虫精进/爬虫阶段练习/6.17/demo.csv','r',newline='',encoding='utf-8')
reader = csv.reader(csv_file)
for row in reader:
    print(row)