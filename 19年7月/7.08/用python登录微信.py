import itchat
itchat.auto_login(hotReload = True)
# 这样，可以延长登录的时间，不必每次都登录。
itchat.send(u'天天happy！', 'filehelper')
friends = itchat.get_friends(update=True)[0:]
for i in friends[1:]:
    print(i["Signature"])