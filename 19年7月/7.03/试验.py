class 出租车():
    # for i in range(3):
    #     print(i)
    def __init__(self,参数):
        self.每公里费用 = 参数    

    def 计费(self):
        公里数 = float(input('请输入行程公里数：'))
        费用 = 公里数 * self.每公里费用
        print('费用一共是：' + str(费用) + '元')

小王的出租车 = 出租车(2.5)
小王的出租车.计费()

小李的出租车 = 出租车(3)
小李的出租车.计费()
