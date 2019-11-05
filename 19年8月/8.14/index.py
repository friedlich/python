"""
课题分享：python骚操作之：微信消息防撤回
主讲老师：老杨老师
开发环境：pycharm + python3
温馨提示：
学习没有太多捷径，但是学习有方式和方法
科学的学习方式和方法可以帮助你更快的学好知识
为了帮助同学们有最大的收获，希望同学们能遵守下面的规则：
第一：不要拘泥于代码  思维远比代码更重要，紧跟老师思维
第二：积极和老师互动，便于老师了解同学们的吸收情况
第三：不懂得问题及时发出来，知道答案的同学主动帮助
编程思维的培养  解决问题的重要
（这是对你的知识的巩固，同时说不定你的答案是错的，
老师就会帮你纠正）
1   2
1。 为了解决某个存在的问题尔诞生的
# 生活化的例子
"""
# 从零基础开始完成项目
# 反问清楚
# 第一 最紧急的需求是什么
# 思路分析
# 微信消息 防撤回
# 肯定要和微信打上交道
# 得到这些消息
# 备份
# 防撤回 -》防数据丢失了
# 文件   误删  备份
# 把数据备份  丢失  备份的消息找出来
# 代码实现
# 定义一个函数
# 安装第三方库
# 标准库
# pip install itchat
# 导入第三方库

import itchat
import re
# 消息注册机制
# 装饰器
# 只要接收到了微信的消息，就自动调用下方的函数
# 函数必须携带一个参数  msg
# 见名知义  英文
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
# 电脑
# 弟弟
# 看
# curd  查看
# 更骚的操作
# 888
# 系统的了解
# 兴趣是最好的老师
# 骚
# 闷骚
# 编程
# 钱多话少死的早
# 七夕活动的最后
# 为了帮助我们的同学 从零开始系统性的全面性学好
# 独自开发企业级项目
# 就业为导向
# 公开课   VIP系统
# 授课老师  -》
# Python  赚钱
# 自学
# 5个月
# 效率
# 工资高  门槛低
# 市场
# 2017年
# 40万
# 1000  500
# 目前   14亿
# 授课
# 视频直播互动
# 2  网络
# 高清的视频录播
# 两年
# web开发
# 5个月
# 项目实战
#
# web
# 47%
# 潭州课堂  视频直播互动
# 晚上直播
# 222
# 从制度
# 授课
# 1 没课堂  课后作业
# 2 分阶段 阶段性的考核  免费重修
# 疑问
# 3大
#  课程研发老师
#  授课老师
#  答题老师团队  解答老师
# 2    弟子
# 跟着
# 666
# 九折
# 7880元 *0.9
# 7880

