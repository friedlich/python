# 第一次
import requests
url = 'https://wordpress-edu-3autumn.localprod.forc.work/wp-login.php'
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
data = {
'log': 'spiderman',  #写入账户
'pwd': 'crawler334566',  #写入密码
'wp-submit': '登录',
'redirect_to': 'https://wordpress-edu-3autumn.localprod.forc.work/wp-admin/',
'testcookie': '1'
}
login_in = requests.post(url,headers=headers,data=data)
#用requests.post发起请求，放入参数：请求登录的网址、请求头和登录参数，然后赋值给login_in。
cookies = login_in.cookies 
#提取cookies的方法：调用requests对象（login_in）的cookies属性获得登录的cookies，并赋值给变量cookies。

url_1 = 'https://wordpress-edu-3autumn.localprod.forc.work/wp-comments-post.php'
data_1 = {
'comment': input('请输入你想要发表的评论：'),
'submit': '发表评论',
'comment_post_ID': '13',
'comment_parent': '0'
}
#把有关评论的参数封装成字典。
comment = requests.post(url_1,headers=headers,data=data_1,cookies=cookies)
#用requests.post发起发表评论的请求，放入参数：文章网址、headers、评论参数、cookies参数，赋值给comment。
#调用cookies的方法就是在post请求中传入cookies=cookies的参数。
print(comment.status_code)
#打印出comment的状态码，若状态码等于200，则证明我们评论成功。

# 虽然我们已经成功发表了评论，但我们的项目到这里还没有结束。因为这个代码还有优化的空间（仅仅是完成还不够，更优雅才是
# 我们该有的追求）。
# 优化这个代码的话，我们需要理解一个新的概念——session（会话）。

# 所谓的会话，你可以理解成我们用浏览器上网，到关闭浏览器的这一过程。session是会话过程中，服务器用来记录特定用户会话的信息。
# 比如你打开浏览器逛购物网页的整个过程中，浏览了哪些商品，在购物车里放了多少件物品，这些记录都会被服务器保存在session中。
# 如果没有session，可能会出现这样搞笑的情况：你加购了很多商品在购物车，打算结算时，发现购物车空无一物Σ(っ°Д°;)っ
# ，因为服务器根本没有帮你记录你想买的商品。
# 对了，session和cookies的关系还非常密切——cookies中存储着session的编码信息，session中又存储了cookies的信息。
# 当浏览器第一次访问购物网页时，服务器会返回set cookies的字段给浏览器，而浏览器会把cookies保存到本地。
# 等浏览器第二次访问这个购物网页时，就会带着cookies去请求，而因为cookies里带有会话的编码信息，服务器立马就能辨认出
# 这个用户，同时返回和这个用户相关的特定编码的session。
# 这也是为什么你每次重新登录购物网站后，你之前在购物车放入的商品并不会消失的原因。因为你在登录时，服务器可以通过浏览器
# 携带的cookies，找到保存了你购物车信息的session。

# 既然cookies和session的关系如此密切，那我们可不可以通过创建一个session来处理cookies？
# 不知道。那就翻阅requests的官方文档找找看有没有这样的方法，能让我们创建session来处理cookies。





