#实现输入10个数字，并打印10个数的求和结果
# a = 1# 控制循环次数
# s = 0#s=0
# while a <= 10:
#     i = int(input("输入数字："))
#     s = s + i #i
#     a = a + 1
# print("求和：",s)
# print(a - 1)

#从键盘依次输入10个数，最后打印最大的数、10个数的和、平均数。
# n = 10# 控制循环次数
# nums = []
# for i in range(n):
#     num = int(input("输入任意整数："))
#     nums.append(num)

#使用random模块，如何产生50~150之间的数？
import random
aa = random.randint(50,150)
# 50 < aa < 150
print("randint:",random.randint(50,150))
