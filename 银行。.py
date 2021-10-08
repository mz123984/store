import random
import aaa

print("==============================================")
print("|-------------中国工商银行账户管理系统------------|")
print("|------------1、开户              ------------|")
print("|------------2、取钱              ------------|")
print("|------------3、存钱              ------------|")
print("|------------4、转账              ------------|")
print("|------------5、查询              ------------|")
print("|------------6、退出              ------------|")
print("==============================================")
bank_name = "小苗仔银行分行"  # 全局变量，有显示就可以调用，如果需要一个全局变量，用global
#bank = {}  # 空数据库

money = 0
# {'m': {'password': '123', 'country': '中国', 'province': '安徽', 'street': '王楼', ' door': '1', 'account': 67960567, 'bank_name': '小苗仔银行分行', 'money': 0}}
def bank_useradd(username, password, country, province, street, door, account):  # bank_useradd起的名字  方法
    #查询是否已满
    sql1 = "select count(*) from miaozai"
    param1 = []
    data = aaa.select(sql1,param1)
    if data[0][0] >= 100:
        return 3
    # 查询是否存在
    sql2 = "select * from miaozai where username = %s"
    param2 = [username]
    data2 = aaa.select(sql2,param2) # ("12345",张三，“nbjhsu”)
    if len(data2) != 0:
        return 2

    #插入数据
    sql3 = "insert into miaozai values(%s,%s,%s,%s,%s,%s,%s,%s,now(),%s)"
    param3 = [account,username,password,country,province,street,door,money,bank_name]
    aaa.update(sql3,param3)
    return 1


def useradd():  # 定义函数要加小括号，不加就错了
    username = input("请输入您的用户名：")
    password = input("请输入您的密码：")  # print(bank[username]["password"])
    print("下面请输入您的地址：")
    country = input("\t\t请输入您所在的国家：")  # \t就是一个tab
    province = input("\t\t请输入您所在的省份：")
    street = input("\t\t请输入您所在的街道：")
    door = input("\t\t请输入您的门牌号：")
    # money=int(input("\t\t请输入您的金额："))
    account = random.randint(10000000, 99999999)
    status = bank_useradd(username, password, country, province, street, door, account)
    if status == 1:
        print("恭喜您成功开户！以下是您的信息")
        info = '''

            ----------个人信息-------------
            用户名：%s
            帐号：%s
            密码：%s
            国家：%s
            省份：%s
            街道：%s
            门牌号：%s
            余额：%s
            开户行名称：%s 
            -------------------------------       
        '''
        print(info % (username, account, password, country, province, street, door, money, bank_name))


# 存钱
def deposit(account, saver):
    sql = "select * from miaozai where account = %s"
    param = [account]
    username = aaa.select(sql,param)
    if account == username[0][0]:
        sql1 = "update miaozai set money = money + %s where account = %s "
        param1 = [int(saver),account]
        money = aaa.update(sql1,param1)
        return "存款成功"
    else:
        return False


# 取钱
def apple(account, password, draw):
    sql = "select * from miaozai where account = %s"
    param = [account]
    username = aaa.select(sql,param)
    if account == username[0][0]:
        if password == username[0][2]:
            if int(draw) <= username[0][7]:
                sql1 = "update miaozai set money = money - %s where account = %s and password = %s and %s <= money"
                param1 = [int(draw),account,password,int(draw)]
                money = aaa.update(sql1,param1)
                return"取款成功！"
    # if account == bank[account]["account"]:
    #     if password == bank[account]["password"]:
    #         if bank[account]["money"] >= draw:
    #             bank[account]["money"] = bank[account]["money"] - draw
    #             return bank[account]["money"]
            else:
                return 3
        else:
            return 2
    else:
        return 1


# 转账
def babyz(account, turn, password, account1):
    sql = "select * from miaozai where account = %s "
    param = [account]
    username = aaa.select(sql,param)
    sql1 = "select * from miaozai where account = %s"
    param1 = [account1]
    username1 = aaa.select(sql1,param1)
    if int(account) == username[0][0]:
        if int(account1) == username1[0][0]:
            if password == username[0][2]:
                if int(turn) <= username[0][7]:
                    sql2 = "update miaozai set money = money - %s where account = %s and password = %s and %s <= money"
                    param2 = [int(turn),account,password,int(turn)]
                    aaa.update(sql2,param2)
                    sql3 = "update miaozai set money = money + %s where account = %s"
                    param3 = [int(turn),account1]
                    aaa.update(sql3,param3)
                    print("转账成功！")


#     if account in list(bank.keys()):
#         if account1 in list(bank.keys()):
#             if password == bank[account]["password"]:
#                 if bank[account]["money"] >= turn:
#                     print(bank[account]["money"], bank[account1]["money"])
#                     bank[account]["money"] = bank[account]["money"] - turn
#                     bank[account1]["money"] = bank[account1]["money"] + turn
#                     print(bank[account]["money"], bank[account1]["money"])
#                     return 0
                else:
                    return 3
        else:
            return 2
    else:
        return 1


# 查询
def demind(account, password):
    sql = "select * from miaozai where account = %s"
    param = [account]
    username = aaa.select(sql,param)
    if account == username[0][0]:
        if password == username[0][2]:
            print("查询成功！")

        else:
            print("密码输入错误")
    else:
        print("该用户不存在")


while True:
    begin = input("请选择业务")
    if begin == "1":
        useradd()

        #print(bank)
    elif begin == "2":
        account = int(input("请输入您的帐号："))
        saver = int(input("请输入您的存款金额："))
        aaa = deposit(account, saver)
        print(aaa)
    elif begin == "3":
        account = int(input("请输入您的帐号："))
        password = int(input("请输入您的密码："))
        draw = int(input("请输入您的取款金额："))
        bbb = apple(account, password, draw)
        print(bbb)
    elif begin == "4":
        account = int(input("请输入您的帐号："))
        account1 = int(input("请输入对方的帐号"))
        turn = int(input("请输入您的转账金额："))
        password = int(input("请输入您的密码："))
        # ccc = bank[account]["money"]
        # eee = bank[account1]["money"]
        riace = babyz(account, turn, password, account1)
        # if riace == 0:
        #     print("ok")
        # elif riace == 1:
        #     print("帐号错误")
        # elif riace == 2:
        #     print("密码不对")
        # elif riace == 3:
        #     print("您的钱不够了啦。")
    elif begin == "5":
        account = int(input("请输入您的帐号："))
        password = int(input("请输入您的密码："))
        ddd = demind(account, password)
        print(ddd)
    elif begin == "6":
        print("退出系统")
        break
    else:
        print("你瞎输入什么东西")
        break

