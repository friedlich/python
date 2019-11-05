import requests,json
url = 'http://ictclas.nlpir.org/nlpir/index6/getWord2Vec.do'
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
words = input('请输入你想查询的词汇：')
data = {'content':words}
res = requests.post(url,data=data,headers=headers)
data=res.text
# 以上，为上一步的代码

data1=json.loads(data)
# 把json数据转换为字典
print ('和“'+words+'”相关的词汇，至少还有：')
# 打印文字
f=0
# 设置变量f
for i in data1['w2vlist']: # 遍历列表
    f=f+1
    word = i.split(',')    # 切割字符串
    print ('('+str(f)+')'+word[0]+'，其相关度为'+word[1]) # 打印数据