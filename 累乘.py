# a = 1  # 控制循环次数
# s = 1
# k = int(input("游戏次数："))
# while a <= k:
#     i = int(input("输入数字："))
#     s = s*i
#     a = a + 1
# print("累乘：", s)


list=[1,2,3,4,5,6,7,8,9]
# print(li[::-1])
list1 = []
i=1
j=8
while i<=len(list):
    list1.append(list[j])
    j-=1
    i+=1
print(list1)


# list2=[5,4,3,2,1,6,7,8,9,10]
#
# print(set(list2))
# print(sorted(list2))
#
# print(list+list2)
