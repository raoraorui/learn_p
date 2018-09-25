# _*_ coding:utf-8 _*_
import threading
import time

def run(n):
    print(n,'1-1开始')
    time.sleep(1)
    print(n, '1-1结束')
    print(n, '1-2开始')
    time.sleep(2)
    print(n, '1-2结束')
    print(n, '1-3开始')
    time.sleep(2)
    print(n, '1-3结束')
    print(n, '1-4开始')
    time.sleep(2)
    print(n, '1-4结束')


t1 = threading.Thread(target=run, args=("t1",))
t2 = threading.Thread(target=run, args=("t2",))
t1.start()
t2.start()