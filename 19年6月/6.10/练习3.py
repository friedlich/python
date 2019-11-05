import requests
res = requests.get('https://static.pandateacher.com/Over%20The%20Rainbow.mp3')
# 发出请求，并把返回的结果放在变量res中
res.encoding = 'utf-8'
mp3=res.content
# 把Reponse对象的内容以二进制数据的形式返回
music = open('rainbow.mp3','wb')
# 新建了一个文件ppt.jpg，这里的文件没加路径，它会被保存在程序运行的当前目录下。
# 图片内容需要以二进制wb读写。你在学习open()函数时接触过它。
music.write(mp3) 
# 获取pic的二进制内容
music.close()
# 关闭文件