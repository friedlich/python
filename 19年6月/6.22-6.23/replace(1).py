# '''
# 把要转换的Query String Parametres参数
# 放在文本里然后执行脚本
# 文本名自定义
# '''
# with open(r'c:/Users/asus/Desktop/Python/风变Python爬虫精进/爬虫阶段练习/6.22-6.23,'a',encoding='utf-8') as g:
#     g.write('\n')

# with  open(r'c:/Users/asus/Desktop/Python/风变Python爬虫精进/爬虫阶段练习/6.22-6.23','r',encoding='utf-8') as f:
#     x = f.readlines()   
import re

x = '''ct: 24
qqmusic_ver: 1298
new_json: 1
remoteplace: txt.yqq.song
searchid: 60507439192682273
t: 0
aggr: 1
cr: 1
catZhida: 1
lossless: 0
flag_qc: 0
p: 2
n: 10
w: 周杰伦
g_tk: 5381
loginUin: 0
hostUin: 0
format: json
inCharset: utf8
outCharset: utf-8
notice: 0
platform: yqq.json
needNewCode: 0'''


k = re.sub('.*', '".*"',x)
print(k)
l = k.replace('\n', '\',')
# print(l)
m = '\'' + l 
# print(m)
    # with open('st1.txt','a',encoding='utf-8') as p:
    #     print(m, file=p)



    




            










# def replace (word):
#     for i in word:
#         a = i 
#         b = word[i]
#         if i == 'pagenum' or i == 'lasthotcommentid':
#             print("'{}': {},".format(a,b))
#         else:
#             print("'{}': '{}',".format(a,b))