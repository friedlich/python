from email.mime.text import MIMEText
from email.header import Header
#引入Header和MIMEText模块
content=input('请输入邮件正文：')
#输入你的邮件正文
message = MIMEText(content, 'plain', 'utf-8')
#实例化一个MIMEText邮件对象，该对象需要写进三个参数，分别是邮件正文，文本格式和编码.
subject = input('请输入你的邮件主题：')
#用input()获取邮件主题  
message['Subject'] = Header(subject, 'utf-8')
#在等号的右边，是实例化了一个Header邮件头对象，该对象需要写入两个参数，分别是邮件主题和编码，
#然后赋值给等号左边的变量message['Subject']。

# 解释一下：第1行和第2行代码是引入了email库中的MIMEText模块和Header模块。

# 第4行代码是用input()函数获取邮件正文，第6行代码是实例化一个MIMEText的邮件对象，这样我们就构造了一个纯文本邮件了。

# 这个MIMEText对象有三个参数，一个是邮件正文；另一个是文本格式，一般设置为plain纯文本格式；最后一个是编码，设置为utf-8，因为utf-8是最流行的万国码。

# 继续看第8行代码，是用input()函数获取邮件主题，第10行代码比较重要，我们仔细讲解一下：
# message['Subject'] = Header(subject, 'utf-8')

# 等号右边是实例化了一个Header邮件头对象，该对象需要写入两个参数，分别是邮件主题和编码。

# 等号左边的message['Subject']的变量是一个a['b']的代码形式，它长得特别像字典根据键取值的表达，
# 但是这里的message是一个MIMEText类的对象，并不是一个字典，那message['Subject']是什么意思呢？

# 其实，字典和类在结构上，有相似之处。请看下图：

# 字典里面的元素是【键】和【值】一一对应，而类里面的【属性名】和【属性】也是一一对应的。我们可以根据字典里的【键】
# 取到对应的【值】，同样的，也可以根据类里面的【属性名】取到【属性】。

# 所以message['Subject']就代表着根据MIMEText类里面的Subject的属性名取到该属性。

# 需要注意的是，不是每一个类都可以这样访问其属性的，之所以能这样访问是因为这个MIMEText的类实现了这个功能。

# 所以，message['Subject'] = Header(subject, 'utf-8') 就是在为message['Subject']这个属性赋值。

# 好啦，到现在，我们就明白如何填写主题和撰写正文了。