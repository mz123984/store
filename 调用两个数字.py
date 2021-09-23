#有以下两个数，使用+，-实现两个数的调换
   #A=56
   #B=78
#实现效果：A=78
#        B=56

#求和法
A=56
B=78
print("A = 56")
print("B = 78")
# A = int(input("第一个整数："))
# B = int(input("第二个整数："))
A = A + B
B = A - B
A = A - B
print("使用求和法得出结果：")
print("A变换后为：",A)
print("B变换后为：",B)
#python内置方法
# print("请输入两个整数：")
# A = int(input("第一个整数："))
# B = int(input("第二个整数："))
# A,B = B,A
# print("使用python内置方法得出结果：")
# print("A变换后为：%d"% A)
# print("B变换后为：%d"% B)



