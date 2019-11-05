# 实例002：“个税计算”
# 题目 企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分
# 按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，
# 可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，
# 求应发放奖金总数？
# 程序分析 分区间计算即可。
profit = int(input('Show me the money:'))
bonus = 0
thresholds = [100000,100000,200000,200000,400000]
rates = [0.1,0.075,0.05,0.03,0.015,0.01]
for i in range(len(thresholds)):
    if profit <= thresholds[i]:
        bonus += profit*rates[i]
        print(bonus)
        profit = 0
        break
    else:
        bonus += thresholds[i]*rates[i]
        print(bonus)
        profit -= thresholds[i]
        print(profit)
bonus += profit*rates[-1]
print(bonus)


