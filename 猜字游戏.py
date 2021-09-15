"""
猜字游戏
需求：
1、猜的数字是系统产生的，不是自己定义的
2、键盘输入的  操作完成填入:input("提示")
3、判断       操作完成填入:if判断条件 elif判断条件
4、循环       操作完成填入:while 条件循环
5、如果你的num>ran 打印猜大了，如果num<ran,则猜小了
6、初始金额为500，每猜中一次扣除100.如果资金为0，退出系统。
7、如果三次都没有猜中，那就退出。
8、如果猜对了，增加10，随机数不能只随机一次。
"""
import random
an=random.randint(0,20)
i = 0
ran = 500
while i <= 7:
    num=int(input("请输入一个数字: "))
    if num > an:
        ran = ran - 100
        print("数字猜大了呦")
    elif num < an:
        ran = ran - 100
        print("数字猜小了呦")
    elif num == an:
        ran = ran + 10
        print("猜对啦！小可爱真棒！",num,ran,"要继续猜下去吗？")
        s = input("请输入Yes或No")
        print(type(s),s)
        if s == "Yes":
            continue
        elif s == "No":
            break
        else:
            break
    if ran <= 0:
        break
    i = i + 1









