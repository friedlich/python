# 3）. 对于用户认识的单词，给选择题让用户做：此处要记录用户做对了哪些，做错了哪些。

# 这一步是第0步和第2步的组合——涉及到第0步中的选择，也涉及到第2步的数据记录。

# 提示： 面对冗长的字典列表相互嵌套，可以创建字典。



# print ('现在我们来检测一下，你有没有真正掌握它们：')
# wrong_words = []
# right_num = 0
# for y in words_knows:
#     print('\n\n'+'A:'+y['definition_choices'][0]['definition'])
#     #我们改用A、B、C、D，不再用rank值，下同
#     print('B:'+y['definition_choices'][1]['definition'])
#     print('C:'+y['definition_choices'][2]['definition'])
#     print('D:'+y['definition_choices'][3]['definition'])
#     xuanze = input('请选择单词\"'+y['content']+'\"的正确翻译：')
#     dic = {'A':y['definition_choices'][0]['rank'],'B':y['definition_choices'][1]['rank'],'C':y['definition_choices'][2]['rank'],'D':y['definition_choices'][3]['rank']} 
#     #我们创建一个字典，搭建起A、B、C、D和四个rank值的映射关系。
#     if dic[xuanze] == y['rank']:
#     #此时dic[xuanze]的内容，其实就是rank值，此时的代码含义已经和之前的版本相同了。
#         right_num += 1
#     else:
#         wrong_words.append(y)

    