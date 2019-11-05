import requests
#引用requests库
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md')
#下载《三国演义》第一回，我们得到一个对象，它被命名为res
novel=res.text
#把Response对象的内容以字符串的形式返回
k = open('《三国演义》.txt','a+')
#创建一个名为《三国演义》的txt文档，指针放在文件末尾，追加内容
k.write(novel)
#写进文件中     
k.close()
#关闭文档