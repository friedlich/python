import requests
url = 'https://www.shanbay.com/api/v1/vocabtest/category/?'
headers = {'referer': 'https://www.shanbay.com/vocabtest/',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
res = requests.get(url,headers=headers)
json_in = res.json()
# print(json_in)
bianhao = int(input('''请输入你想测试的词库的编号：(按Enter确认) 
1，GMAT  2，考研  3，高考  4，四级  5，六级
6，英专  7，托福  8，GRE  9，雅思  10，任意
'''))

ciku = json_in['data'][bianhao-1][0]
url_test = 'https://www.shanbay.com/api/v1/vocabtest/vocabularies/?'
params = 'category=ciku'
res_test = requests.get(url_test,headers=headers,params=params)
words = res_test.json()
# print(words)

danci = []
words_knows = []
not_knows = []
print ('测试现在开始。如果你认识这个单词，请输入Y，否则直接敲Enter：')
n=0
for i in words['data']:
    n=n+1
    print ("\n第"+str(n)+'个：'+i['content'])
    answer = input('认识请敲Y，否则敲Enter：')
    if answer == 'Y':
        danci.append(i['content'])
        words_knows.append(i)
    else:
        not_knows.append(i)   
print ('\n在上述'+str(len(words['data']))+'个单词当中，有'+str(len(danci))+'个是你觉得自己认识的，它们是：')
print(danci)

print ('现在我们来检测一下，你有没有真正掌握它们：')
wrong_words = []
right_num = 0
for j in words_knows: #你要看清楚了啊，这个地方你根本就没有理解，word_knows不是仅仅存单词的列表，它是和data等价的列表，里面有很多东西的
    print('\n\n'+'A:'+j['definition_choices'][0]['definition'])
    print('B:'+j['definition_choices'][1]['definition'])
    print('C:'+j['definition_choices'][2]['definition'])
    print('D:'+j['definition_choices'][3]['definition'])
    xuanze = input('请选择单词\"'+j['content']+'\"的正确翻译：')
    dic = {'A':j['definition_choices'][0]['rank'],'B':j['definition_choices'][1]['rank'],'C':j['definition_choices'][2]['rank'],'D':j['definition_choices'][3]['rank']} 
    if dic[xuanze] == j['rank']:
        right_num += 1
    else:
        wrong_words.append(j)

print ('现在，到了公布成绩的时刻:')
print ('在'+str(len(words['data']))+'个'+json_in['data'][bianhao-1][1]+'词汇当中，你认识其中'+str(len(danci))+'个，实际掌握'+str(right_num)+'个，错误'+str(len(wrong_words))+'个。')
save = input ('是否打印并保存你的错词集？填入Y或N： ')
if save == 'Y':
    f = open(r'c:/Users/asus/Desktop/Python/风变Python爬虫精进/爬虫阶段练习/6.20/错题集.txt', 'a+')
    print ('你记错的单词有：')
    f.write('你记错的单词有：\n')
    m=0
    for z in wrong_words:
        m=m+1
        print (z['content'])
        #打印每一个错词。
        f.write(str(m) +'. '+ z['content']+'\n')
    print ('你不认识的单词有：')
    f.write('你没记住的单词有：\n')
    s=0
    for x in not_knows:
        s=s+1
        print (x['content'])
        f.write(str(s) +'. '+ x['content']+'\n')
    print ('错词和没记住的词已保存至当前文件目录下，下次见！')
else:
    print('下次见！')
    


    



