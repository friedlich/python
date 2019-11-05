# 该模块适用于配置文件的格式与windows ini文件类似，可以包含一个或多个节（section），每个节可以有多个参数（键=值）。
# 节与java原先的配置文件相同的格式

# 看一下configparser生成的配置文件的格式
# [DEFAULT]
# ServerAliveInterval = 45
# Compression = yes
# CompressionLevel = 9
# ForwardX11 = yes
  
# [bitbucket.org]
# User = Atlan
  
# [topsecret.server.com]
# Port = 50022
# ForwardX11 = no

## 现在看一下类似上方的配置文件是如何生成的
import configparser #引入模块

config = configparser.ConfigParser()    #类中一个方法 #实例化一个对象

config["DEFAULT"] = {'ServerAliveInterval': '45',
                      'Compression': 'yes',
                     'CompressionLevel': '9',
                     'ForwardX11':'yes'
                     }	#类似于操作字典的形式

config['bitbucket.org'] = {'User':'Atlan'} #类似于操作字典的形式

config['topsecret.server.com'] = {'Host Port':'50022','ForwardX11':'no'}

with open(r'c:/Users/asus/Desktop/Python/风变Python爬虫精进/爬虫阶段练习/19年7月/7.08/example.ini', 'w') as configfile:

   config.write(configfile)	#将对象写入文件

# 解释一下，操作方式
config["DEFAULT"] = {'ServerAliveInterval': '45',
                      'Compression': 'yes',
                     'CompressionLevel': '9',
                     'ForwardX11':'yes'
                     }	#类似于操作字典的形式
#config后面跟的是一个section的名字，section的段的内容的创建类似于创建字典。类似与字典当然还有别的操作方式啦！
config['bitbucket.org'] = {'User':'Atlan'}  #类似与最经典的字典操作方式
# 和字典的操作方式相比，configparser模块的操作方式，无非是在实例化的对象后面，跟一个section，在紧跟着设置section的属性
# （类似字典的形式）

## 读文件内容
import configparser

config = configparser.ConfigParser()

#---------------------------查找文件内容,基于字典的形式

print(config.sections())        #  []

config.read(r'c:/Users/asus/Desktop/Python/风变Python爬虫精进/爬虫阶段练习/19年7月/7.08/example.ini')

print(config.sections())        #   ['bitbucket.org', 'topsecret.server.com']


print('bytebong.com' in config) # False
print('bitbucket.org' in config) # True


print(config['bitbucket.org']["user"])  # Atlan

print(config['DEFAULT']['Compression']) #yes

print(config['topsecret.server.com']['ForwardX11'])  #no


print(config['bitbucket.org'])          #<Section: bitbucket.org>

for key in config['bitbucket.org']:     # 注意,有default会默认default的键
    print(key)

print(config.options('bitbucket.org'))  # 同for循环,找到'bitbucket.org'下所有键

print(config.items('bitbucket.org'))    #找到'bitbucket.org'下所有键值对

print(config.get('bitbucket.org','compression')) # yes       get方法Section下的key对应的value





