#任务：
# 尽量多的添加商品
# 10个辣条优惠券(0,3)，20滑板优惠券(0,9)
#在进入商城时，随机抽取优惠券，在最后结算使用该优惠券。
import random
#1，商品
shop = [
    #   0      1
    ["国风滑板",200],  # 0  print(shop(0))=["国风滑板",200]  print(shop[0][1])=200
    ["冷面老鸭手机壳",30],  # 1
    ["<<撒野>>实体书全套",104],  # 2
    ["MAC",170],  # 3
    ["祖马龙香水",330],  # 4
    ["小迷糊面膜",70],  # 5
    ["卫龙小辣条",40],  # 6
    ["韩风小画本",20],  # 7
    ["马克笔64色",40],  # 8
    ["黄色小台灯",66],  # 9
    ["足球",100],  # 10
    ["跳绳",26]  # 11
]
#print(shop)
#2,初始化金额
moeny = int(input("呦！客官，请输入您的铜钱嘿："))



#3，空的购 物车
mycart = []
print("客官何不来一张优惠券？")
s = input("请输入中或不可:")
if s == "中":
    card = random.randint(1,31)
    if card <=10:
        print("卫龙小辣条优惠券一张")
        shop[6][1] = 0.3*shop[6][1]
    else:
        print("国风滑板优惠券一张")
        shop[0][1] = 0.9*shop[0][1]
else:
    s == "不可"
    print("")






# 4，购买
while True:#永远循环

    for index,value in enumerate(shop):#枚举，把角标和角标对应的内容进行整体打印
        print(index,value[0],"",value[1])#打印所有的商品
    chose = input("客官挑一个")#int 如果一开始就是数字，那么下面的if就没有意义
    if chose.isdigit():#isdigit 判断是否为数字
        chose = int(chose)
        if chose > len(shop) - 1:
            print("本店没有这个呦~")
            break
        else:
            if moeny > shop[chose][1]:
                mycart.append(shop[chose])
                moeny = moeny - shop[chose][1]
                print("恭喜客官获得心爱之物哦~")
            else:
                print("死鬼，买不起，快去挣钱！")
                break
             #    import random
             #    a = index,value[6]
             # a = random.randint(0,10)
    elif chose == "A" or chose == "a":
            print("客官下次再来呦，下面是您的单子")
            for index,value in enumerate(mycart):
                print(index,"",value[0],"",value[1])
            print("客官您的铜钱还有：",moeny,"元")
            break
    else:
        print("哒美哒美，不可以呦~")
