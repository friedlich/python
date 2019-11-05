import os,sys,csv
print(os.getcwd())
a = 'shiyan3'
with open(sys.path[0]+'\\'+a+'.csv','w',newline='',encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(['今天','明天','后天'])
    writer.writerow(['美好的','事情','会来到'])
with open(os.getcwd()+'\\19年7月\\7.12\\shiyan1.csv','w',newline='',encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(['今天','明天','后天'])
    writer.writerow(['美好的','事情','会来到'])



import sys
print(sys.path[0])
print(sys.path[0],end='')
# print(sys.path)
['c:\\Users\\asus\\Desktop\\Python\\风变Python基础语法\\python小课作业代码\\06.02', 
    'C:\\Users\\asus\\AppData\\Local\\Programs\\Python\\Python36\\python36.zip', 
        'C:\\Users\\asus\\AppData\\Local\\Programs\\Python\\Python36\\DLLs', 
            'C:\\Users\\asus\\AppData\\Local\\Programs\\Python\\Python36\\lib', 
                'C:\\Users\\asus\\AppData\\Local\\Programs\\Python\\Python36', 
                    'C:\\Users\\asus\\AppData\\Roaming\\Python\\Python36\\site-packages', 
                        'C:\\Users\\asus\\AppData\\Local\\Programs\\Python\\Python36\\lib\\site-packages', 
                            'C:\\Users\\asus\\AppData\\Local\\Programs\\Python\\Python36\\lib\\site-packages\\pip-19.1.1-py3.6.egg', 
                                'C:\\Users\\asus\\AppData\\Local\\Programs\\Python\\Python36\\lib\\site-packages\\win32', 
                                    'C:\\Users\\asus\\AppData\\Local\\Programs\\Python\\Python36\\lib\\site-packages\\win32\\lib', 
                                        'C:\\Users\\asus\\AppData\\Local\\Programs\\Python\\Python36\\lib\\site-packages\\Pythonwin']
import sys
for i in sys.path:
    print(i)