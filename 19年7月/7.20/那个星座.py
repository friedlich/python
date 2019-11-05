import datetime,time

def check_input(infor):
    sexs = ['man','woman']
    if len(infor.split()) != 3:
        print(u'请输入信息个是如下：man 20 1-1 or woman 30 4-9')
        return False,''
    elif infor.split()[0] not in sexs:
        print(u'你输入的{}格式不正确，请输入 man or woman'.format(infor.split()[0]))
        return False,''
    elif int(infor.split()[1]) not in range(20,61): # 单单一个(20,61)是一个元组，当然不行，必须是年龄包含在这个范围内
        print(int(infor.split()[1]))
        print(u'你输入的年龄{}不在范围内，请输入年龄范围20-60岁'.format(infor.split()[1]))
        return False,''
    elif not is_date_valid(infor.split()[-1]):
        print(u'你输入的生日日期不正确，请输入 month-day'.format(infor.split()[-1]))
        return False,''
    else:
        return True,infor.split()

def is_date_valid(date_str):
    if datetime.datetime.strptime(date_str,'%m-%d'):
        return True
    else:
        return False

def get_constellation_by_birthday(month, day):
    '''
	1.摩羯座12.22-1.19 Capricorn
	2.水瓶座1.20-2.18  Aquarius
	3.双鱼座2.19-3.20  Pisces
    4.白羊座3.21-4.20  Aries
    5.金牛座4.21-5.20  Taurus
    6.双子座5.21-6.21  Gemini
    7.巨蟹座6.22-7.22  Cancer
    8.狮子座7.23-8.22  Leo
    9.处女座8.23-9.22  Virgo
    10.天秤座9.23-10.22 Libra
    11.天蝎座10.23-11.21 Scorpio
    12.射手座11.22-12.21 Sagittarius
	'''
    constellation_name_list = [u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座',
                               u'金牛座', u'双子座', u'巨蟹座', u'狮子座',
                               u'处女座', u'天秤座', u'天蝎座', u'射手座']
    constellation_date_range = [(1, 20), (2, 19), (3, 21), (4, 21),
                                (5, 21), (6, 22), (7, 23), (8, 23),
                                (9, 23),(10, 23), (11, 22), (12, 22)]
    res = list(filter(lambda each_constellation: each_constellation <= (month, day), constellation_date_range))
    print(res)
    print(len(res))
    return constellation_name_list[len(res)%12]

def get_woman_date_choice(your_age):
    woman_choice_25 = [u'帅气', u'个子高']
    woman_choice_30 = [u'有钱', u'事业有成']
    woman_choice_35 = [u'稳重', u'有责任心']
    woman_choice_40 = [u'对我好', u'有共同的生活目标']
    woman_choice_50 = [u'身体健康', u'顾家']
    woman_choice_60 = [u'有共同语言']
    woman_chocies = [woman_choice_25, woman_choice_30, woman_choice_35,
                     woman_choice_40, woman_choice_50, woman_choice_60]
    woman_ages = [25, 30, 35, 40, 50, 60]
    res = list(filter(lambda age: age < your_age, woman_ages))
    print(res)
    print(len(res))
    return woman_chocies[len(res)]

def woman_man_constellation_mapping(your_constellation):
    constellation_mapping_dict = {u'白羊座': [u'狮子座', u'白羊座', u'金牛座'],
                                  u'金牛座': [u'处女座', u'摩羯座', u'巨蟹座'],
                                  u'双子座': [u'水瓶座', u'射手座', u'天秤座'],
                                  u'巨蟹座': [u'双鱼座', u'天蝎座', u'摩羯座'],
                                  u'狮子座': [u'射手座', u'白羊座', u'水瓶座'],
                                  u'处女座': [u'摩羯座', u'金牛座', u'双鱼座'],
                                  u'天秤座': [u'双子座', u'水瓶座', u'狮子座'],
                                  u'天蝎座': [u'双鱼座', u'处女座', u'射手座'],
                                  u'射手座': [u'白羊座', u'狮子座', u'双子座'],
                                  u'摩羯座': [u'金牛座', u'处女座', u'双鱼座'],
                                  u'水瓶座': [u'天秤座', u'双子座', u'狮子座'],
                                  u'双鱼座': [u'天蝎座', u'巨蟹座', u'摩羯座']}
    print(constellation_mapping_dict.get(your_constellation))
    return constellation_mapping_dict.get(your_constellation)

def get_man_date_choice(your_age):
    man_choice = [u'年轻', u'漂亮']
    man_choice_dict = {'20-60': man_choice}
    if your_age >= 20 and your_age <= 60:
        return man_choice

if __name__ == '__main__':
    while True:
        infor = input(u'>请输入你的性别(man,woman)，年龄(20-60)，生日(month-day)\n>例如:man 20 1-1 or woman 30 3-2：\n')
        print(int(infor.split()[1]))
        is_input_ok,input_info = check_input(infor)
        print(input_info)

        if is_input_ok:
            print(u'匹配...')
            time.sleep(1)
            sex,age,birthday = input_info
            print(sex,age,birthday)
            birthday_month,birthday_day = list(map(int,birthday.split('-')))
            print(birthday_month,birthday_day)
            your_constellation = get_constellation_by_birthday(birthday_month,birthday_day)
            if sex == 'woman':
                print('{} {}岁 {} 心仪男:{} 匹配星座:{}'.format(u'女', age, your_constellation, 
                ','.join(get_woman_date_choice(int(age))), ','.join(woman_man_constellation_mapping(your_constellation))))
            
            if sex == 'man':
                print('{} {}岁 {} 心仪女孩:{} 匹配星座:{}'.format(u'男', age, your_constellation, 
                ','.join(get_man_date_choice(int(age))), ','.join(woman_man_constellation_mapping(your_constellation))))

        exit = input('>please input q exit or input Enter will continue!\n')
        if exit == 'q':
                print('exit....')
                break



        

