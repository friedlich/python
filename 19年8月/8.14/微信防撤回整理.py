import itchat
import re

data_list = dict()

@itchat.msg_register(['Text','Picture','Recording','Video'])
def message(msg):
    print(msg)
    # 获取消息的类型
    type = msg['Type']
    # 取出MsgId，作为保存的编号
    MsgId  = msg['MsgId']
    # 取出微信的消息，去除左右的空格

    # 友好一点 提升用户体验度
    # 找出用户的昵称
    name = itchat.search_friends(userName=msg['FromUserName'])['NickName']
    # 思考：我需要保存那些信息
    # 用户消息谁发的
    # 开始把消息存起来
    # 1   2
    # 字典的键是不能重复的
    # 覆盖的消息  让键不唯一
    if type=='Text':
        content = msg['Text'].strip()
    else:
    # itchat的附件下载方法存储在msg的Text键中
    # # 将文件下载下来
        msg['Text'](msg['FileName'])
        content = msg['FileName']
    global data_list
    data_list[MsgId] = {'name':name,'content':content,'type':type}
    # 在撤回了消息的时候，吧消息找出来
# 作用域
# 表示只要接收到微信通知就自动调用下发的函数
# 全局  局部
# 666 劳逸结合
@itchat.msg_register(['Note'])
def message(msg):
    print(msg)
    if '撤回了一条消息' in msg['Text']:
        old_msg_id = re.search('\<msgid\>(.*?)\<\/msgid\>',msg['Content']).group(1)
        # 找出昵称
        name = data_list[old_msg_id]['name']
        type = data_list[old_msg_id]['type']
        # 找出内容
        content = data_list[old_msg_id]['content']
        # 反摩擦
        toUserName = itchat.search_friends(nickName=name)[0]['UserName']
        if type=='Text':
            # 把消息发送出去
            itchat.send(content,'filehelper')
            itchat.send(content,toUserName)
            print(content)
        else:
            filename = "@fil@" + content
            itchat.send(filename, 'filehelper')
            itchat.send(filename,toUserName)

#
# 1   2

def main():
    # 占位符
    # 先登录
    # bug   拜祭四爷  专治八阿哥
    # 大量的调试   公开课
    # 避免重复扫码   itchat.pkl
    try:
        itchat.auto_login(hotReload=True)
    except Exception as err:
        exit()
    # 获取到我的微信消息
    itchat.run()
# 主程序的入口
# 方便我们的代码调试
if __name__ == '__main__':
    # 调用一个函数
    main()
