'''
把要转换的Query String Parametres参数
放在文本里然后执行脚本
文本名自定义
'''
with open('st.txt','a',encoding='utf-8') as g:
    g.write('\n')

with  open('st.txt','r',encoding='utf-8') as f:
    x = f.readlines()   

for i  in range(len(x)):
    j = x[i]
    k = j.replace(': ', '\': \'')
    l = k.replace('\n', '\',')
    m = '\'' + l 
    with open('st1.txt','a',encoding='utf-8') as p:
        print(m, file=p)



    




            










# def replace (word):
#     for i in word:
#         a = i 
#         b = word[i]
#         if i == 'pagenum' or i == 'lasthotcommentid':
#             print("'{}': {},".format(a,b))
#         else:
#             print("'{}': '{}',".format(a,b))