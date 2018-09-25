# _*_ coding:utf-8 _*_

def outer(x):
    y = [1,2,3]
    def inner():
        print (x)
        print (y)
    return inner
x = 5    #这个x没有被引用
f = outer(2)
f()
print (f.__closure__)   #函数属性__closure__存储了函数的环境变量