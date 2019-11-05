import requests,json,sys

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
url = 'https://www.shanbay.com/api/v1/vocabtest/category/'
print('''1.GMAT  2.考研  3.高考  4.四级  5.六级  
6.英专  7.托福  8.GRE   9.雅思  10.任意''')
choose = int(input('请选择你要测试内容的序号：'))
res = requests.get(url,headers=headers)
json_type = json.loads(res.text)
type = json_type['data'][choose-1][0]
print(type)
url = 'https://www.shanbay.com/api/v1/vocabtest/vocabularies/?category='+type
res = requests.get(url,headers=headers)
json_words = json.loads(res.text)
danci = []
words_knows = []
not_knows = []
print('测试现在开始，如果你认识这个单词的话，请敲Y，否则直接敲Enter继续：')
n=0
for data in json_words['data']:
    n+=1
    print('\n第'+str(n)+'个单词：'+data['content'])
    answer = input('认识请敲Y，否则敲Enter: ')
    if answer == 'Y':
        danci.append(data['content'])
        words_knows.append(data)
    else:
        not_knows.append(data)

print('\n在上述{}个单词中，有{}个是你觉得自己认识的，它们是：'.format(str(n),str(len(danci))))
print(danci)

print('现在我们来测试一下，你有没有掌握他们：')
wrong_words = []
right_num = 0
for i in words_knows:
    print('\n'+'A:',i['definition_choices'][0]['definition'])
    print('B:',i['definition_choices'][1]['definition'])
    print('C:',i['definition_choices'][2]['definition'])
    print('D:',i['definition_choices'][3]['definition'])
    xuanze = input('请输入单词\"'+i['content']+'\"的正确翻译：')
    dic = {'A':i['definition_choices'][0]['rank'],'B':i['definition_choices'][1]['rank'],'C':i['definition_choices'][2]['rank'],'D':i['definition_choices'][3]['rank']}
    if dic[xuanze] == i['rank']:
        right_num+=1
    else:
        wrong_words.append(i)

print('现在，到了公布成绩的时候了：')
print('在{}个{}词汇当中，你认识其中{}个，实际掌握{}个，错误{}个'.format(len(json_words['data']),json_type['data'][choose-1][1],len(danci),str(right_num),len(wrong_words)))

save = input('是否打印并保存你的错题集？填入Y或N：')
if save == 'Y':
    with open(sys.path[0]+'\\错题集.txt','w') as f:
        print('你记错的单词有：')
        f.write('你记错的单词有：\n')
        m=0
        for i in wrong_words:
            m+=1
            print(i['content'])
            f.write(str(m)+'. '+i['content']+'\n')
        print('你不认识的单词有：')
        f.write('你没记住的单词有: \n')
        s=0
        for j in not_knows:
            s+=1
            print(j['content'])
            f.write(str(s)+'. '+j['content']+'\n')
        print('错词和没记住的单词已保存至相应目录下，请查收,下次见！')
else:
    print('下次见！')
