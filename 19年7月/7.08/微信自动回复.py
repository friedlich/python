import itchat
import requests
def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'   #改成你自己的图灵机器人的api，上图红框中的内容，不过用我的也无所谓，只是每天自动回复的消息条数有限
    data = {
        'key': 'cc808f580b7a4b7caaa9f1f31e6d602e',  # Tuling Key 
        'info': msg,  # 这是我们发出去的消息
        'userid': 'wechat-robot',  # 这里你想改什么都可以
    }
    # 我们通过如下命令发送一个post请求
    r = requests.post(apiUrl, data=data).json()
    return r.get('text')
@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    return get_response(msg['Text'])
@itchat.msg_register([itchat.content.TEXT], isGroupChat=True)
def print_content(msg):
    return get_response(msg['Text'])
itchat.auto_login(True)
itchat.run()

# 大致原理简介：
# 用到两个库，一个itchat，一个requests，如果你import itchat 没用出异常，也说明你之前安装itchat库成功啦，requests是网络请求库，python自带的，用于调用图灵机器人API 
# @itchat.msg_register(itchat.content.TEXT)：用于接收来自朋友间的对话消息  #如果不用这个，朋友发的消息便不会自动回复 
# @itchat.msg_register([itchat.content.TEXT], isGroupChat=True)：用于接收群里面的对话消息
# 实现原理也很简单，接受到信息，调用get_response（）方法，把消息传给图灵机器人，然后接收的回复信息再返回给微信，大致是这个原理
# 最后是登录接口的调用，执行itchat.auto_login（），执行的python代码，会弹出一个登录二维码，类似网页端的扫码登录，你扫码登录后，就会由机器人替你处理朋友以及群里发来的消息啦，当然，如果不希望机器处理，你退出网页端的登录即可