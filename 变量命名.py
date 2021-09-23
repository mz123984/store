#判断变量命名是否合法
#变量名，通常是由字母、数字和下划线构成，可以随意组合，但不能以数字打头，中文字符也支持 。
while True:
    m = input("请输入变量名：")
    if m == "exit":
        print("欢迎下次使用。")
        break
    if m[0].isalpha() or m[0] == "_":
        for i in m[1:]:
            if not(i.isalnum() or i == "_"):
                print("变量名不合法" )
                break
        else:
            print("变量名合法" )
    else:
        print("变量名不合法" )


