'''
需求：3个厨师造汉堡，每造一个向篮子里扔一个，当篮子已经满了的时候，停3秒，判断是否已满，
没满，继续造汉堡。
有6个程序员，每个汉堡5元。
6个人同时抢，当篮子汉堡不够，稍等3秒，然后判断篮子里是否还有，直到钱花完为止。
'''
from threading import Thread
import time
bread = 0
money = 50

class chef(Thread):
    username1 = ""
    def run(self) -> None:
        global bread,money  # 申明使用全局变量
        while True:
            if bread < 10 and money>0:
                time.sleep(1)
                bread = bread + 1
                print(self.username1,"做了",bread,"个小面包！")
            elif bread >= 10 and money>0:
                time.sleep(3)
            elif money <= 0:
                break

class person(Thread):
    username = ""
    count = 0  # 个数
    def run(self) -> None:
        global bread,money
        while True:
            if bread > 0:
                bread = bread - 1
                self.count = self.count + 1  # ???
                money = money - 5
                print(self.username,"抢了",self.count,"花了",5 * self.count)
            if money <= 0:
                print("没钱啦！")
                break
            elif bread <= 0:
                time.sleep(3)



m1 = chef()
m2 = chef()
m3 = chef()

m1.username1 = "胡歌"
m2.username1 = "彭于晏"
m3.username1 = "杨洋"

p1 = person()
p2 = person()
p3 = person()
p4 = person()
p5 = person()
p6 = person()

p1.username = "苗儿"
p2.username = "倩儿"
p3.username = "依依"
p4.username = "玲儿"
p5.username = "媛儿"
p6.username = "洁儿"

m1.start()
m2.start()
m3.start()

p1.start()
p2.start()
p3.start()
p4.start()
p5.start()
p6.start()









