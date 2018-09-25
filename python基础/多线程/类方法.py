# _*_ coding:utf-8 _*_
import threading
import time



class MyThread(threading.Thread):

    def __init__(self, n):
        super(MyThread, self).__init__()  # 重构run函数必须要写
        self.n = n

    def run(self):
        print(self.n, '1-1开始')
        time.sleep(1)
        print(self.n, '1-1结束')
        print(self.n, '1-2开始')
        time.sleep(2)
        print(self.n, '1-2结束')
        print(self.n, '1-3开始')
        time.sleep(2)
        print(self.n, '1-3结束')
        print(self.n, '1-4开始')
        time.sleep(2)
        print(self.n, '1-4结束')


if __name__ == "__main__":
    t1 = MyThread("t1")
    t2 = MyThread("t2")

    t1.start()
    t2.start()