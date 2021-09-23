#编程实现下列图形的打印
lines = int(input("输入要打印的行数："))
for i in range(lines):
    for j in range(0,lines - i):
        print(end=" ")#空格！好神奇！
    for k in range(2 * i + 1):
        print("*",end="")
    print()