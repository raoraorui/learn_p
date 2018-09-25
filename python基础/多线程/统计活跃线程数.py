# _*_ coding:utf-8 _*_
import threading
import time


"""
def run(n):
    print("task", n)
    time.sleep(1)       #此时子线程停1s

for i in range(3):
    t = threading.Thread(target=run, args=("t-%s" % i,))
    t.start()

time.sleep(0.5)     #主线程停0.5秒
print(threading.active_count()) #输出当前活跃的线程数
"""






def run(n):
    print("task", n)
    time.sleep(0.5)       #此时子线程停0.5s


for i in range(3):
    t = threading.Thread(target=run, args=("t-%s" % i,))
    t.start()

time.sleep(1)     #主线程停1秒
print(threading.active_count()) #输出活跃的线程数，到这一步其它的子线程都已经完成，所有只剩一个主线程