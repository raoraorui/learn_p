# _*_ coding:utf-8 _*_
import threading
import time


def run(n):
    print("task", n, threading.current_thread())  # 输出当前的线程
    time.sleep(1)
    print('3s')
    time.sleep(1)
    print('2s')
    time.sleep(1)
    print('1s')


strat_time = time.time()

t_obj = []  # 定义列表用于存放子线程实例

for i in range(3):
    t = threading.Thread(target=run, args=("t-%s" % i,))
    t.start()
    t_obj.append(t)



for tmp in t_obj:
    tmp.join()  # 为每个子线程添加join之后，主线程就会等这些子线程执行完之后再执行。

print("cost:", time.time() - strat_time)  # 主线程

print(threading.current_thread())  # 输出当前线程