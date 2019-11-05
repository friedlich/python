# 设计数据结构的时候，字典是必须的！很多时候我们会用带下面的字典更新的方法，
# 当然更好的是collections模块里面的defaultdict!

options = {'code':'utf-8'}
base_headers = {'User-Agent': 100,
                'Accept-Encoding': 'gzip,deflate,sdch',
                'Accept-Language': 'zh-CN,zh;q=0.8'}
# 会生成一个新的字典
headers = dict(base_headers,**options)
print(headers)
# 或者用update,更新原来的字典
base_headers.update(options)
print(base_headers)
# 点评：dict.update还是比较平易近人的，这个dict(dict,**options)用法我第一次看到的时候也是楞了一些，
# 什么鬼，现在见多了，也就习惯了！

# Python入门容易精通难，平时遇到优秀的代码一定要勤做笔记，不定时拿出来翻一翻，一定对你功力增长大有裨益！

