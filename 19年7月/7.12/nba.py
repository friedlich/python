# 在本次实验环境中，我们将会使用到 python 的pandas，numpy，scipy和sklearn库，实验楼的在线环境中都已经具备，无需手动安装。
# 接下来，我们下载相应的数据文件并解压。

# # 获取数据文件
# !wget http://labfile.oss.aliyuncs.com/courses/782/data.zip
# # 安装 unzip
# !apt-get install unzip
# # 解压data压缩包并且删除该压缩包
# !unzip data.zip 
# !rm -r data.zip

# 在data文件夹中，包含了 2015~2016 年的 NBA 数据 T,O 和 M 表，及经处理后的常规赛和挑战赛的比赛数据2015-2016_result.csv，这个数据文件是我们通过在basketball-reference.com的 2015-2016 Schedule and result 的几个月份比赛数据中提取得到的，其中包括三个字段：
#     WTeam: 比赛胜利队伍
#     LTeam: 失败队伍
#     WLoc: 胜利队伍一方所在的为主场或是客场
# 另外一个文件就是16-17Schedule.csv，也是经过我们加工处理得到的 NBA 在 2016-2017 年的常规赛的比赛安排，其中包括两个字段：
#     Vteam: 客场作战队伍
#     Hteam: 主场作战队伍

# 代码实现
# 下载完实验数据后，就可以正式开始实验了

# 首先，引入实验相关模块：
import pandas as pd
import math
import csv
import random
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import cross_val_score

# 设置回归训练时所需用到的参数变量
# 当每支队伍没有elo等级分时，赋予其基础elo等级分
base_elo = 1600
team_elos = {} 
team_stats = {}
X = []
y = []
# 存放数据的目录
folder = 'data2015' 

# 在最开始需要初始化数据，从 T、O 和 M 表格中读入数据，去除一些无关数据并将这三个表格通过Team属性列进行连接：
# 根据每支队伍的Miscellaneous Opponent，Team统计数据csv文件进行初始化
def initialize_data(Mstat, Ostat, Tstat):
    new_Mstat = Mstat.drop(['Rk', 'Arena'], axis=1)
    new_Ostat = Ostat.drop(['Rk', 'G', 'MP'], axis=1)
    new_Tstat = Tstat.drop(['Rk', 'G', 'MP'], axis=1)

    team_stats1 = pd.merge(new_Mstat, new_Ostat, how='left', on='Team')
    team_stats1 = pd.merge(team_stats1, new_Tstat, how='left', on='Team')
    return team_stats1.set_index('Team', inplace=False, drop=True)

# 获取每支队伍的Elo Score等级分函数，当在开始没有等级分时，将其赋予初始base_elo值：
def get_elo(team):
    try:
        return team_elos[team]
    except:
        # 当最初没有elo时，给每个队伍最初赋base_elo
        team_elos[team] = base_elo
        return team_elos[team]

# 定义计算每支球队的Elo等级分函数：
# 计算每个球队的elo值
def calc_elo(win_team, lose_team):
    winner_rank = get_elo(win_team)
    loser_rank = get_elo(lose_team)

    rank_diff = winner_rank - loser_rank
    exp = (rank_diff  * -1) / 400
    odds = 1 / (1 + math.pow(10, exp))
    # 根据rank级别修改K值
    if winner_rank < 2100:
        k = 32
    elif winner_rank >= 2100 and winner_rank < 2400:
        k = 24
    else:
        k = 16

    # 更新 rank 数值
    new_winner_rank = round(winner_rank + (k * (1 - odds)))      
    new_loser_rank = round(loser_rank + (k * (0 - odds)))
    return new_winner_rank, new_loser_rank

# 基于我们初始好的统计数据，及每支队伍的 Elo score 计算结果，建立对应 2015~2016 年常规赛和季后赛中每场比赛的数据集（在主客场比
# 赛时，我们认为主场作战的队伍更加有优势一点，因此会给主场作战队伍相应加上 100 等级分）：
def  build_dataSet(all_data):
    print("Building data1 set..")
    X = []
    skip = 0
    for index, row in all_data.iterrows():

        Wteam = row['WTeam']
        Lteam = row['LTeam']

        #获取最初的elo或是每个队伍最初的elo值
        team1_elo = get_elo(Wteam)
        team2_elo = get_elo(Lteam)

        # 给主场比赛的队伍加上100的elo值
        if row['WLoc'] == 'H':
            team1_elo += 100
        else:
            team2_elo += 100

        # 把elo当为评价每个队伍的第一个特征值
        team1_features = [team1_elo]
        team2_features = [team2_elo]

        # 添加我们从basketball reference.com获得的每个队伍的统计信息
        for key, value in team_stats.loc[Wteam].iteritems():
            team1_features.append(value)
        for key, value in team_stats.loc[Lteam].iteritems():
            team2_features.append(value)

        # 将两支队伍的特征值随机的分配在每场比赛数据的左右两侧
        # 并将对应的0/1赋给y值
        if random.random() > 0.5:
            X.append(team1_features + team2_features)
            y.append(0)
        else:
            X.append(team2_features + team1_features)
            y.append(1)

        if skip == 0:
            print('X',X)
            skip = 1

        # 根据这场比赛的数据更新队伍的elo值
        new_winner_rank, new_loser_rank = calc_elo(Wteam, Lteam)
        team_elos[Wteam] = new_winner_rank
        team_elos[Lteam] = new_loser_rank

    return np.nan_to_num(X), y

# 最终在 main 函数中调用这些数据处理函数，使用 sklearn 的Logistic Regression方法建立回归模型：
if __name__ == '__main__':
    
    Mstat = pd.read_csv(r'c:\Users\asus\Desktop\Python\风变Python爬虫精进\爬虫阶段练习\19年7月\7.12\data2015\15-16Miscellaneous_Stat.csv')
    Ostat = pd.read_csv(r'c:\Users\asus\Desktop\Python\风变Python爬虫精进\爬虫阶段练习\19年7月\7.12\data2015\15-16Opponent_Per_Game_Stat.csv')
    Tstat = pd.read_csv(r'c:\Users\asus\Desktop\Python\风变Python爬虫精进\爬虫阶段练习\19年7月\7.12\data2015\15-16Team_Per_Game_Stat.csv')

    team_stats = initialize_data(Mstat, Ostat, Tstat)

    result_data = pd.read_csv(r'c:\Users\asus\Desktop\Python\风变Python爬虫精进\爬虫阶段练习\19年7月\7.12\data2015\2015-2016_result.csv')
    X, y = build_dataSet(result_data)

    # 训练网络模型
    print("Fitting on %d game samples.." % len(X))

    model = linear_model.LogisticRegression()
    model.fit(X, y)

    # 利用10折交叉验证计算训练正确率
    print("Doing cross-validation..")
    print(cross_val_score(model, X, y, cv = 10, scoring='accuracy', n_jobs=-1).mean())

# 最终利用训练好的模型在 16~17 年的常规赛数据中进行预测。
# 利用模型对一场新的比赛进行胜负判断，并返回其胜利的概率：
def predict_winner(team_1, team_2, model):
    features = []

    # team 1，客场队伍
    features.append(get_elo(team_1))
    for key, value in team_stats.loc[team_1].iteritems():
        features.append(value)

    # team 2，主场队伍
    features.append(get_elo(team_2) + 100)
    for key, value in team_stats.loc[team_2].iteritems():
        features.append(value)

    features = np.nan_to_num(features)
    return model.predict_proba([features])

# 在 main 函数中调用该函数，并将预测结果输出到16-17Result.csv文件中：
# 利用训练好的model在16-17年的比赛中进行预测

print('Predicting on new schedule..')
schedule1617 = pd.read_csv(r'c:\Users\asus\Desktop\Python\风变Python爬虫精进\爬虫阶段练习\19年7月\7.12\data2015\16-17Schedule.csv')
result = []
for index, row in schedule1617.iterrows():
    team1 = row['Vteam']
    team2 = row['Hteam']
    pred = predict_winner(team1, team2, model)
    prob = pred[0][0]
    if prob > 0.5:
        winner = team1
        loser = team2
        result.append([winner, loser, prob])
    else:
        winner = team2
        loser = team1
        result.append([winner, loser, 1 - prob])

with open(r'c:\Users\asus\Desktop\Python\风变Python爬虫精进\爬虫阶段练习\19年7月\7.12\16-17Result1.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['win', 'lose', 'probability'])
    writer.writerows(result)
    print('done.')

# 最后，我们实验 Pandas 预览生成预测结果文件16-17Result.csv文件：
pd.read_csv(r'c:\Users\asus\Desktop\Python\风变Python爬虫精进\爬虫阶段练习\19年7月\7.12\16-17Result1.csv',header=0)

# 实验总结
# 在本节课程中，我们利用Basketball-reference.com的部分统计数据，计算每支 NBA 比赛队伍的Elo socre，和利用这些基本统计数据评
# 价每支队伍过去的比赛情况，并且根据国际等级划分方法Elo Score对队伍现在的战斗等级进行评分，最终结合这些不同队伍的特征判断在一
# 场比赛中，哪支队伍能够占到优势。但在我们的预测结果中，与以往不同，我们没有给出绝对的正负之分，而是给出胜算较大一方的队伍能够
# 赢另外一方的概率。当然在这里，我们所采用评价一支队伍性能的数据量还太少（只采用了 15~16 年一年的数据），如果想要更加准确、系
# 统的判断，有兴趣的你当然可以从各种统计数据网站中获取到更多年份，更加全面的数据。结合不同的回归、决策机器学习模型，搭建一个更
# 加全面、预测准确率更高的模型。在 kaggle 中有相关的篮球预测比赛项目，有兴趣的同学可尝试一下。

###
# FileNotFoundError: [Errno 2] File b'data2015/15-16Miscellaneous_Stat.csv' does not exist: b'data2015/15-16Miscellaneous_Stat.csv'
# FileNotFoundError: [Errno 2] File b'data2015\r-16Miscellaneous_Stat.csv' does not exist: 
# b'data2015\r-16Miscellaneous_Stat.csv'
# FileNotFoundError: [Errno 2] File b'data2015\\15-16Miscellaneous_Stat.csv' does not exist:
# b'data2015\\15-16Miscellaneous_Stat.csv'


