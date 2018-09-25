# _*_ coding:utf-8 _*_
import threading
import time

gl_num = 0

lock = threading.RLock()


def Func():
    lock.acquire()
    global gl_num
    gl_num += 1
    time.sleep(1)
    print(gl_num)

    lock.release()


for i in range(10):
    t = threading.Thread(target=Func)
    t.start()