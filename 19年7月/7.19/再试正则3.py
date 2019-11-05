a = '<em>45afaf?:;<em>'
import re
# b = re.sub('A-Za-z[\d\?]','',a)
# b = re.sub('[A-Za-z\d\?]','',a)
b = re.sub('[A-Za-z\d\?\<\>]','',a) ##所有的秘密都是源于一个中括号，不然的话等于是把前面好不容易除去的字符又填回来了
print(b)
import re
content = '龙卷风 - <em>周杰伦</em> (Jay Chou)\n 词：徐若瑄\n 曲：<em>周杰伦</em>\n 编曲：<em>周杰伦</em>\n 制作人：<em>周杰伦</em>\n 爱像一阵风 吹完它就走\n 这样的节奏 谁都无可奈何\n 没有你以后 我灵魂失控\n 黑云在降落 我被它拖着走\n 静静悄悄默默离开\n 陷入了危险边缘Baby\n 我的世界已狂风暴雨 wu\n 爱情来的太快 就像龙卷风\n 离不开暴风圈 来不及逃\n 我不能再想 我不能再想\n 我不 我不 我不能\n 爱情走的太快 就像龙卷风\n 不能承受 我已无处可躲\n 我不要再想 我不要再想\n 我不 我不 我不要再想你\n 不知不觉 你已经离开我\n 不知不觉 我跟了这节奏'
lyrics = content.replace(' ','').replace('\\n','\n')
print(lyrics)
# an= re.sub('[\<\>\[em]\/]','',lyrics) 
an = re.sub('[\<>\/\()]','',lyrics)
an = re.sub('em','',an)
print(an) #这他妈可终于弄完了呀，方法有很多很多，主要是看你理解的怎么样，特别是一些细节问题