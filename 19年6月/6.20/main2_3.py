# （2）. 让用户选择认识的单词：此处，要分别记录下用户认识哪些，不认识哪些。

# 已经有了单词数据，提取出来让用户识别，并记录用户认识哪些不认识哪些，至少2个list来记录。
# 50个单词，记得要用循环。
# 用户手动输入自己的选择，用input() 。
# 我们要识别用户的输入，并基于此决定把这个单词放进哪个list，需要用if语句。

# 提示：当一个元素特别长的时候，给代码多加一个list。
# 提示：加个换行，优化用户视角。



# danci = []
# #新增一个list，用于统计用户认识的单词
# words_knows = []
# #创建一个空的列表，用于记录用户认识的单词。
# not_knows = []
# #创建一个空的列表，用于记录用户不认识的单词。
# print ('测试现在开始。如果你认识这个单词，请输入Y，否则直接敲Enter：')
# n=0
# for x in words['data']:
# #启动一个循环，循环的次数等于单词的数量。
#     n=n+1
#     print ("\n第"+str(n)+'个：'+x['content'])
#     #加一个\n，用于换行。
#     answer = input('认识请敲Y，否则敲Enter：')
#     #让用户输入自己是否认识。
#     if answer == 'Y':
#     #如果用户认识：
#         danci.append(x['content'])
#         words_knows.append(x)
#         #就把这个单词，追加进列表words_knows。
#     else:
#     #否则
#         not_knows.append(x)
#         #就把这个单词，追加进列表not_knows。


# print ('\n在上述'+str(len(words['data']))+'个单词当中，有'+str(len(danci))+'个是你觉得自己认识的，它们是：')
# print(danci)