import pymysql
conn = pymysql.connect(host='localhost',user='root',password='123456',port=3306,db='mysql')
cursor = conn.cursor()
print(cursor.execute('select * from db'))
print(cursor.fetchone())