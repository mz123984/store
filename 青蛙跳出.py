#一只青蛙掉在井里了，井高20米，青蛙白天往上爬3米，晚上滑下2米，问第几天能出来?用编程求出。
#应该用到什么呢？
high = -20
up = 3
down = -2
num = 1
while high < 0:
    print('day',num,end="  ")
    high += up
    print("up",high,end="  ")
    if high >= 0:
        break
    high += down
    print("down",high)
    if high >= 0:
        break
    num += 1
