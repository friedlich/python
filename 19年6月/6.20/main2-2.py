# （1）. 根据选择的题库，获取50个单词。

# 第0步我们已经拿到链接，这步直接用requests去下载，re.json()解析即可。


# ciku = js_link['data'][bianhao-1][0]
#利用用户输入的数字编号，获取题库的代码。如果以输入“高考”的编号“3”为例，那么ciku的值就是，在字典js_link中
#查找data的值，data是一个list，查找它的第bianhao-1，也就是第2个元素，得到的依然是一个list，再查找该list
#的第0个元素。最后得到的就是我们想要的NCEE。
# test = requests.get('https://www.shanbay.com/api/v1/vocabtest/vocabularies/?category='+ciku)
#下载用于测试的50个单词。
# words = test.json()
#对test进行解析。