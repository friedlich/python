import requests,json
url = 'http://ictclas.nlpir.org/nlpir/index6/getWord2Vec.do'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
words = input('请输入你感兴趣的内容：')
data = {
    'content': words
}
res = requests.post(url,headers=headers,data=data)
json_words = json.loads(res.text)
print('与'+words+'相关的词汇有：')
for i in json_words['w2vlist']:
    word = i.split(',')
    print(word[0])

