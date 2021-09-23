#1,使用while循环实现99乘法表的打印
# i = 1
# while i<= 9:
#     j = 1
#     while j <= i:
#         sum = j*i
#         print("%dx%d=%2d"%(j,i,sum),end=("\t"))
#         j += 1
#     print()
#     i += 1


#2,单列，第一列
# a = 1
# while a < 10:
#     b = 1
#     while b < 10:
#         print("%d*%d = %d"%(a,b,a*b))
#         b += 1
#         a += 1

#3,编程实现99乘法表的倒叙打印
i = 9
while i>=1:
    k = 1
    while k <= 9-i:
        print("     ",end="\t")
        k += 1
    j = 1
    while j<=i:
        print("%dx%d=%2d"%(j,i,j*i),end=("\t"))
        j += 1
    print()
    i -= 1


