# coding=utf-8
import datetime,time

def get_man_date_choice(your_age):
    man_choice = ['young', 'beautiful']
    man_choice_dict = {'20': man_choice}
    if your_age >= 20 and your_age <= 60:
        return man_choice


def get_woman_date_choice(your_age):
    woman_choice_25 = ['Handsome', 'Higher']
    woman_choice_30 = ['Richer', 'Good_career']
    woman_choice_35 = ['Steady', 'Responsible']
    woman_choice_40 = ['Nice', 'SameLifeGoal']
    woman_choice_50 = ['Healthy', 'Be_family']
    woman_choice_60 = ['CommonLanguage']
    woman_chocies = [woman_choice_25, woman_choice_30, woman_choice_35,
                     woman_choice_40, woman_choice_50, woman_choice_60]
    woman_ages = [25, 30, 35, 40, 50, 60]

    res = list(filter(lambda age: age < your_age, woman_ages))
    if len(res) >= len(woman_chocies):
        return woman_chocies[len(res) - 1]
    else:
        return woman_chocies[len(res)]


def get_constellation_by_birthday(month,day):
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
    constellation_name_list = ['Capricorn', 'Aquarius', 'Pisces', 'Aries',
                               'Taurus', 'Gemini', 'Cancer', 'Leo',
                               'Virgo', 'Libra', 'Scorpio', 'Sagittarius']
    constellation_date_range = [(1, 20), (2, 19), (3, 21), (4, 21),
                                (5, 21), (6, 22), (7, 23), (8, 23),
                                (9, 23),(10, 23), (11, 22), (12, 22)]

    res = list(filter(lambda each_constellation: each_constellation <= (month, day), constellation_date_range))

    return constellation_name_list[len(res) % 12]


def woman_man_constellation_mapping(your_constellation):
    constellation_mapping_dict = {'Aries': ['Leo', 'Aries', 'Taurus'],
                                  'Taurus': ['Virgo', 'Capricorn', 'Cancer'],
                                  'Gemini': ['Aquarius', 'Sagittarius', 'Libra'],
                                  'Cancer': ['Pisces', 'Scorpio', 'Capricorn'],
                                  'Leo': ['Sagittarius', 'Aries', 'Aquarius'],
                                  'Virgo': ['Capricorn', 'Taurus', 'Pisces'],
                                  'Libra': ['Gemini', 'Aquarius', 'Leo'],
                                  'Scorpio': ['Pisces', 'Virgo', 'Sagittarius'],
                                  'Sagittarius': ['Aries', 'Leo', 'Gemini'],
                                  'Capricorn': ['Taurus', 'Virgo', 'Pisces'],
                                  'Aquarius': ['Libra', 'Gemini', 'Leo'],
                                  'Pisces': ['Scorpio', 'Cancer', 'Capricorn']}
    return constellation_mapping_dict.get(your_constellation)


def check_input(agrs):
    sexs = ['man', 'woman']
    if len(args.split()) != 3:
        print('Your input error: format as :such as man 20 1998-1-1 or woman 30 1986-4-9')
        return False, ''
    elif args.split()[0] not in sexs:
        print('Your input sex {0} is not legal,please input man or woman'.format(args.split()[0]))
        return False, ''
    elif int(args.split()[1]) not in range(20,61):
        print('Your input age {0} is not legal,please input age range<20,60>'.format(args.split()[1]))
        return False, ''
    elif not is_date_valid(agrs.split()[-1]):
        print('Your input birthday {} is not valid,format as month-day'.format(args.split()[-1]))
        return False, ''
    else:
        return True, agrs.split()


def is_date_valid(date_str):
    try:
        datetime.datetime.strptime(date_str, "%m-%d")
        return True
    except:
        return False


if __name__ == '__main__':

    while True:
        # args = raw_input('>Please input your info:sex[man,woman],age[20..60],birthday[month-day]\n')
        args = input('>Please input your info:sex[man,woman],age[20..60],birthday[month-day]\n')
        is_input_ok, input_info = check_input(args)

        if is_input_ok:
            print('Mating....')
            time.sleep(1)
            sex, age, birthday = input_info
            birthday_month, birthday_day = map(int,birthday.split('-'))
            your_constellation = get_constellation_by_birthday(birthday_month, birthday_day)
            if sex == 'woman':
                print("{0}'s age {1} {2} want to find '{3}' man in {4} constellations". \
                    format(sex, age, your_constellation,','.join(get_woman_date_choice(int(age))),
                           ','.join(woman_man_constellation_mapping(your_constellation))))
            if sex == 'man':
                print("{0}'s age {1} {2} want to find girl '{3}' in {4} constellations". \
                    format(sex, age,your_constellation ,','.join(get_man_date_choice(int(age))),
                           ','.join(woman_man_constellation_mapping(your_constellation))))

        # exit = raw_input('>please input q exit or input Enter will continue!\n')
        exit = input('>please input q exit or input Enter will continue!\n')
        if exit == 'q':
            print('exit....')
            break