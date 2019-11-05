import re , requests , os

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
'Host': 'sh.lianjia.com'
}
def downloadpic(html,keyword):

    pic_url = re.findall('"objURL":"(.*?)"',html)
    #pic_url = re.findall('"objURL":"(.*?)"',html)
    print(pic_url[0:3])
    i = 0
    print('找到关键词：' + keyword +'的图片，现在开始下载图片···')
    for j in pic_url[0:10]:
        print('正在下载第'+str(i+1)+'张图片，图片地址：'+str(j))
        try:
            pic = requests.get(j, timeout = 10)
        except requests.exceptions.ConnectionError:
            print ('【错误】当前图片无法下载')
            continue
        string = keyword+'-'+str(i+1)+'.jpg'
        with open(r'C:\Users\asus\Desktop\Python\风变Python爬虫精进\爬虫阶段练习\19年8月\8.06' + '\\' + word + '\\'+ string,'wb') as fp:
            fp.write(pic.content) #想取文本数据可以通过response.text 如果想取图片，文件，则可以通过 response.content
        i += 1
if __name__ == '__main__':
    word = input('请输入你想下载的图片类型：')
    url = 'http://image.baidu.com/search/index?ct=201326592&tn=baiduimage&word=' + word +'&pn=0&ie=utf-8&oe=utf-8&cl=2&lm=-1&fr=&se=&sme=&hd=1&latest=0&copyright=0'
    res = requests.get(url)
    # os.makedirs(os.path.join("F:\\baidupic",word)) #创建新文件夹
    os.makedirs(os.path.join(r'C:\Users\asus\Desktop\Python\风变Python爬虫精进\爬虫阶段练习\19年8月\8.06',word))
    # print(res.text)
    downloadpic(res.text,word)