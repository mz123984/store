#用循环来实现20以内的数的阶乘。（1！+2！+3！+...+20!)
m = 0
myarray = range(1,21)
def myfunction(x):
    r = 1
    for i in range(1,x + 1):
        r*= i
    return r
sumValue = sum(map(myfunction,myarray))
print("1！+2！+3！+...+20! = %d"% sumValue)