import codecs
import csv
import jieba.analyse
import matplotlib.pyplot as plt
from pyecharts import options as opts
from pyecharts.globals import SymbolType
from pymongo import MongoClient
from pyecharts import Pie, Bar, Map,Line
from pyecharts import WordCloud
import re
import jieba
import numpy as np
import pandas as pd

# 淘宝商品标准excel文件保存路径
GOODS_STANDARD_EXCEL_PATH = r'D:\python\爬虫\数据分析\taobao.csv'
# 读取标准数据
DF_STANDARD = pd.read_csv(GOODS_STANDARD_EXCEL_PATH)
#链接数据库
def mogodb():
    client = MongoClient('localhost', 27017)
    db = client.qxpdb
    collection = db.taobao

#查询库中数据
    results = collection.find()
    return results
#提取数据  并清洗数据
def standard_data():
    for data in mogodb():
        title=data['mingcheng'].replace('\n', '').replace(' ', '')
        prics=data["jiage"]
        sales=data["xiaoliang"]
        sales = sales.replace('+', '').replace('人付款','')
        if '万' in sales:
            sales = sales[:-1]
            if '.' in sales:
                sales = sales.replace('.', '') + '000'
            else:
                sales = sales + '0000'
        raw_location=data["fahuo"]
        location_list = []
        if ' ' in raw_location:
        
            new_location = raw_location[:raw_location.find(' ')]
            location_list.append(new_location)
        #print(new_location)
        else:
            new_location=raw_location
            location_list.append(new_location)
    
        location= location_list[0]
        print([title,prics,sales,location])
        with codecs.open(r'D:\python\爬虫\数据分析\taobao.csv', 'a', 'utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([title,prics,sales,location])
        GOODS_STANDARD_EXCEL_PATH=r'D:\python\爬虫\数据分析\taobao.csv'
    return GOODS_STANDARD_EXCEL_PATH
'''def readcsv():#读取标题
    title=[]
    with open(r'D:\python\爬虫\数据分析\taobao.csv',newline = '')  as f:
        reader = csv.reader(f)
        for row in reader: 
            title.append(row[0])
    return title
    '''

def analysis_title():#词云

    from pyecharts import WordCloud
    from wordcloud import WordCloud
    from wordcloud import STOPWORDS
    global DF_STANDARD
    keywords_count_list = jieba.analyse.textrank(' '.join(DF_STANDARD.title), topK=50, withWeight=True)#jieba分词  并提取出频率前50的词
    print(keywords_count_list)#
    #print(type(keywords_count_list))
    stopWords = STOPWORDS.copy()#屏蔽词
    stopWords.add('睡衣')
    stopWords.add('情趣')
    stopWords.add('情趣内衣')
    wc = WordCloud(width=1524, 
                scale=2,
                height=1068,                
                max_words=50,
                stopwords=stopWords,
                background_color='white',  
                font_path='STKAITI.TTF')                
    wc.generate_from_text(str(keywords_count_list))
    plt.imshow(wc)
    plt.axis('off')         # 不显示坐标轴
    plt.show()              # 显示图像
    wc.to_file(r'D:\python\爬虫\数据分析\图\淘宝标题高频词词云.jpg')
    return keywords_count_list#返回高频词列表

def title():#高频词和商品数目的关系
    global DF_STANDARD
    #global keywords_count_list
                                                                                    #i[0]=高频词  i类型为元组
    keywords_count_dict = {i[0]: 0 for i in reversed(keywords_count_list[:20])}#创建i[0]为键，0为值 即包含20个key为高频词，值为0的字典    {key1：0，key2：0，...,key20:0}
    cut_words = jieba.cut(' '.join(DF_STANDARD.title))#对全部标题进行结巴分词
    for word in cut_words: #word为分词列表提取出来的一个分词
        for keyword in keywords_count_dict.keys():#keyword=高频词
            if word == keyword:#keywords_count_dict[keyword]原本的值为0  如果标题分词等于高频词  即keywords_count_dict[keyword]+1  即0开始+1  到循环结束
                keywords_count_dict[keyword] = keywords_count_dict[keyword] + 1#遍历所有标题 如果有 则加1
    print(keywords_count_dict)#打印各个高频词 在标题中出现的次数
    
    keywords_count_bar = Bar("淘宝商品数据可视化","",width=1000,height=700)
    x_data=list(keywords_count_dict.keys())
    y_data=list(keywords_count_dict.values())
    keywords_count_bar.add("情趣服装商品标题词频分析TOP20", x_data, y_data,is_convert = True,is_label_show=True,xaxis_name='商品数',label_pos= 'right',yaxis_name="分类",yaxis_name_gap=50)
    keywords_count_bar.render(r'D:\python\爬虫\数据分析\图\商品标题词频分析TOP20树状图.html')

def sales():#标题高频关键字与平均销量关系
    global DF_STANDARD
    #global keywords_count_list                  
    keywords_column_dict = {i[0]: [] for i in reversed(keywords_count_list[:20])}#i 为元组类型  []利用两次 一次把将标题包含关键字的属性值放在列表中
    for row in DF_STANDARD.iterrows():#row[0]=id  row class=元组                         第二次存放平均值  妙！！
        for keyword in keywords_column_dict.keys():#keywords_column_dict.keys()=([])  keyword=str
            if keyword in row[1].title:
                # 2、 将标题包含关键字的销量属性值放在列表中，dict={'keyword1':[属性值1,属性值2,..]}
                keywords_column_dict[keyword].append(row[1]['sales'])
    #print(keywords_column_dict[keyword])#keywords_column_dict[keyword]
    for keyword in keywords_column_dict.keys():
        keyword_column_list = keywords_column_dict[keyword]#两次赋值  此时keywords_column_list=[销量1，销量2]
        keywords_column_dict[keyword] = int(sum(keyword_column_list) / len(keyword_column_list))#此时keywords_column_list=[平均销量]
        #print(keywords_column_dict[keyword])
    #print(keywords_column_dict)
    keywords_count_bar = Bar("淘宝商品数据可视化","",width=1500,height=700)
    x_data=list(keywords_column_dict.keys())
    y_data=list(keywords_column_dict.values())
    keywords_count_bar.add("情趣服装商品分类与平均销量TOP20", x_data, y_data,is_label_show=True,yaxis_name='平均销量',xaxis_name="分类",yaxis_name_gap=50)
    keywords_count_bar.render(r'D:\python\爬虫\数据分析\图\分类与平均销量TOP20.html')
    

def price():#标题高频关键字与平均销量关系
    global DF_STANDARD
    #global keywords_count_list                  
    keywords_column_dict = {i[0]: [] for i in reversed(keywords_count_list[:20])}#i 为元组类型  []利用两次 一次把将标题包含关键字的属性值放在列表中
    for row in DF_STANDARD.iterrows():#row[0]=id  row class=元组                         第二次存放平均值  妙！！
        for keyword in keywords_column_dict.keys():#keywords_column_dict.keys()=([])  keyword=str
            if keyword in row[1].title:
                # 2、 将标题包含关键字的属性值放在列表中，dict={'keyword1':[属性值1,属性值2,..]}
                keywords_column_dict[keyword].append(row[1]['price'])
    #print(keywords_column_dict[keyword])#keywords_column_dict[keyword]
    for keyword in keywords_column_dict.keys():
        keyword_column_list = keywords_column_dict[keyword]#两次赋值  此时keywords_column_list=[销量1，销量2]
        keywords_column_dict[keyword] = sum(keyword_column_list) / len(keyword_column_list)#此时keywords_column_list=[平均销量]
        #print(keywords_column_dict[keyword])
    #print(keywords_column_dict)
    keywords_count_bar = Bar("淘宝商品数据可视化","",width=1000,height=700)
    x_data=list(keywords_column_dict.keys())
    y_data=list(keywords_column_dict.values())
    keywords_count_bar.add("情趣服装商品分类与平均价格TOP20", x_data, y_data,is_convert = True,is_label_show=True,label_pos= 'right',yaxis_name='平均价格',xaxis_name="分类",yaxis_name_gap=50)
    keywords_count_bar.render(r'D:\python\爬虫\数据分析\图\分类与平均价格TOP20.html')

def qujian():
    global DF_STANDARD
 
    keywords_count = Pie("淘宝商品数据可视化","",width=1000,height=700,title_top= 'bottom')
    x_data=['0-10元', '11-20元', '21-30元', '31-40元', '41-50元', '51-60元', '61-70元', '71-80元','81-90元', '91-100元', '100元以上']
    y_data=['102','325','280','477','507','485','170','70','53','30','99']
    keywords_count.add("情趣服装商品价格区间和销量关系", x_data, y_data,is_label_show=True,yaxis_name='价格区间/元',xaxis_name="销量",yaxis_name_gap=50)
    keywords_count.render(r'D:\python\爬虫\数据分析\图\商品价格区间和销量关系饼状图.html')

def qujian1():
    global DF_STANDARD
 
    keywords_count_bar = Bar("淘宝商品数据可视化","",width=1000,height=700)#,title_top= 'bottom')
    x_data=['五百以内','五百到一千', '一千到两千','两千到五千', '五千到一万','一万到五万','五万以上' ]
    y_data=['2050','225','121','76','18','13','0']
    keywords_count_bar.add("情趣服装商品销量区间和销量关系", x_data, y_data,is_label_show=True,label_pos= 'top',xaxis_name='销量区间/件',yaxis_name="销量",yaxis_name_gap=50)
    keywords_count_bar.render(r'D:\python\爬虫\数据分析\图\商品销量区间和销量关系树状图.html')   
qujian1()

def analysis_price_sales():
    """
    商品价格与销量关系分析
    :return:
    """
    # 引入全局数据
    global DF_STANDARD
    df = DF_STANDARD.copy()
    df['group'] = pd.qcut(df.price, 12)
    df.group.value_counts().reset_index()
    df_group_sales = df[['sales', 'group']].groupby('group').mean().reset_index()
    df_group_str = [str(i) for i in df_group_sales['group']]
    #a=re.match('.*?(4.8).*','df_group_str[0][0]')
    #df_group_str[0][0]=a[0]
    print(df_group_str)
    sales_list=[]
    #print(list(df_group_sales['sales']))
    for i in list(df_group_sales['sales']):
        a=int(i)
        sales_list.append(a)
    #print(sales_list)
    keywords_count_bar = Bar("淘宝商品数据可视化","",width=1000,height=700)
    x_data=df_group_str
    y_data=sales_list
    keywords_count_bar.add("情趣服装商品价格与平均销量关系", x_data, y_data,is_convert = False,is_label_show=True,label_pos= 'top',xaxis_name='商品价格/元',yaxis_name="平均销量",yaxis_name_gap=50)
    keywords_count_bar.render(r'D:\python\爬虫\数据分析\图\商品价格与平均销量关系树状图.html')



def diqu():
    global DF_STANDARD
    province_sales = DF_STANDARD.location.value_counts()
    province_sales_list = [list(item) for item in province_sales.items()]#item=元组
    #print(province_sales_list)
    x_data=[]
    y_data=[]
    for i in province_sales_list:
        x=i[0]
        y=i[1]
        x_data.append(x)
        y_data.append(y)
    print(y_data)  
    print(x_data)  
    province_sales_map = Map("淘宝商品数据可视化",width=1200, height=600,title_color="#fff")
    province_sales_map.add("前两千五百款情趣内衣商家数量全国分布图", x_data,y_data,"china",visual_range=[0, 200],is_label_show=True,is_visualmap=True,visual_text_color='#000', is_map_symbol_show=False)
    
    province_sales_map.render(r'D:\python\爬虫\数据分析\图\商家数量全国分布图热力图.html')
    # 1.2 生成柱状图
#diqu()    
def b():#商品销量TOP20 名称
    global DF_STANDARD
    data=DF_STANDARD.head(20)
    a=data.sort_values(by='sales', ascending=True)
    x_data=[]
    y_data=[]
    for i in a['title']:
        x_data.append(i)
    for b in a['sales']:
        y_data.append(b)
    keywords_count_bar = Bar("淘宝商品数据可视化","",width=1000,height=500)
    
    keywords_count_bar.add("情趣内衣商品销量TOP20定价", x_data, y_data,is_convert = True,is_label_show=True,yaxis_pos='right',label_pos= 'left',xaxis_name="销量",yaxis_name_pos='end',xaxis_name_pos='end',yaxis_name_gap=50)
    keywords_count_bar.render(r'D:\python\爬虫\数据分析\图\商品销量TOP20树状图.html')

def c():#商品销量TOP20价格定位
    global DF_STANDARD
    data=DF_STANDARD.head(20)
    a=data.sort_values(by='sales', ascending=True)
    x_data=[]
    y_data=[]
    for i in a['price']:
        x_data.append(i)
    for b in a['sales']:
        y_data.append(b)
    keywords_count_bar = Bar("淘宝商品数据可视化","",width=1000,height=500)
    
    keywords_count_bar.add("情趣内衣商品销量TOP20定价", x_data, y_data,is_convert = True,is_label_show=True,yaxis_pos='left',label_pos= 'right',xaxis_name="销量",yaxis_name='定价',yaxis_formatter='元',yaxis_name_gap=50)
    keywords_count_bar.render(r'D:\python\爬虫\数据分析\图\商品销量TOP20价格树状图.html')
def d():#商品销量TOP20商家分布
    global DF_STANDARD
    data=DF_STANDARD.head(20)
    a=data.sort_values(by='sales', ascending=True)
    x_data=[]
    y_data=[]
    for i in a['location']:
        x_data.append(i)
    for b in a['sales']:
        y_data.append(b)
    keywords_count_bar = Pie("淘宝商品数据可视化","",width=1000,height=500)
    
    eywords_count_bar.add("情趣内衣商品销量TOP20商家分布", x_data, y_data,is_convert = True,is_label_show=True,yaxis_pos='left',label_pos= 'right',xaxis_name="销量",yaxis_name='省份',yaxis_name_gap=50)
    keywords_count_bar.render(r'D:\python\爬虫\数据分析\图\商品销量TOP20商家分布树状图.html')
    #province_sales_map = Map("淘宝商品数据可视化",width=1200, height=600,title_color="#fff")
    #province_sales_map.add("情趣内衣商品销量TOP20商家分布", x_data,y_data,"china",visual_range=[0, 200],is_label_show=True,is_visualmap=True,annot=True,visual_text_color='#000', is_map_symbol_show=True)
    #province_sales_map.render(r'D:\python\爬虫\数据分析\图\商品销量TOP20商家分布热力图.html')

def e():#全国商家省份销量总和分布
    data = DF_STANDARD.pivot_table(index='location', values='sales', aggfunc=np.sum)#np.sum为求和 默认平均值
    # 根据销量排序
    #提取location和sales两列分析
    
    x_data=list(data.index)
    y_data=list(data.values)
    
    keywords_count = Pie("情趣服装商品全国商家省份销量总和","",width=1000,height=700,title_top= 'bottom')
    
    keywords_count.add("情趣服装商品全国商家省份销量总和", x_data, y_data,is_label_show=True)
    keywords_count.render(r'D:\python\爬虫\数据分析\图\商品全国商家省份销量总和分布.html')
    
def f():#全国商家省份销量总和分布
    data = DF_STANDARD.pivot_table(index='location', values='sales',aggfunc=np.mean)
    # 根据销量排序
    
    
    x_data=list(data.index)
    a=list(data.values)
    y_data=[]
    print(x_data)
    print(a[6])
    for y in a:
        y_data.append(int(y))
    print(y_data)
    
    

    province_sales_map = Bar("淘宝商品数据可视化",width=1200, height=600,title_color="#fff")
    province_sales_map.add("情趣服装商品全国商家省份平均销量分布", x_data,y_data,is_label_show=True)
    province_sales_map.render(r'D:\python\爬虫\数据分析\图\商品全国商家省份平均销量分布树状图.html')
f()