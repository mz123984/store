# 实现登陆系统的三次密码输入错误锁定功能（用户名：root 密码：admin）
username = "root"
password = "admin"
a = 0
while a < 3:
    c = input("请输入用户名：")
    b = input("请输入密码：")
    if c == username and b == password:
        print("登陆成功!")
    else:
        print("登陆失败！")
        a = a + 1
        if a == 3:
            print("该用户已被锁定")

# 用户名输入错误可以无限次重新输入，输入正确之后再输入密码，密码有三次输入机会。
# username = "小苗仔"
# password = "521"
# while True:
#     a = input("请输入用户名：")
#     if a == username:
#         print("用户名输入成功！")
#         c = 0
#         while c < 3:
#             b = input("请输入密码：")
#             if b == password:
#                 print("登录成功！")
#             else:
#                 print("登录失败！")
#                 c = c + 1
#     else:
#         print("用户名输入失败！")
#     break









