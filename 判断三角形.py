#从键盘输入任意三边，判断是否能形成三角形。
#若可以，则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。）
a = int(input("输入三角形的一边："))
b = int(input("输入三角形的一边："))
c = int(input("输入三角形的一边："))
if(a + b > c and a - c < b)or(a + c > b and a - b < c)or(b + c > a and b - a < c):
    print("构成三角形")
    if a == b or b == c or a == c:
            print("构成等腰三角形")
    elif(a == b and b== c and a == c ):
            print("构成等边三角形")
    elif(a*a + b*b == c*c) or (b*b + c*c == a*a) or (a*a + c*c == b*b):
            print("构成直角三角形")
    else:
            print("构成普通三角形")
else:
    print("不能构成三角形")

