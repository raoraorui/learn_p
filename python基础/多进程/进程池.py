# -*- coding:utf-8 -*-

import os, time
from multiprocessing import Pool


def worker(arg):
    print("子进程开始执行>>> pid={},ppid={},编号{}".format(os.getpid(), os.getppid(), arg))
    time.sleep(1)
    print("子进程终止>>> pid={},ppid={},编号{}".format(os.getpid(), os.getppid(), arg))


def main():
    print("主进程开始执行>>> pid={}".format(os.getpid()))
    ps = Pool(5)
    for i in range(10):
        ps.apply(worker,args=(i,))          # 同步执行
        #ps.apply_async(worker, args=(i,))  # 异步执行

    # 关闭进程池，停止接受其它进程
    ps.close()
    # 阻塞进程
    ps.join()
    print("主进程终止")


if __name__ == '__main__':
    main()
'''
异步执行结果
主进程开始执行>>> pid=4612
子进程开始执行>>> pid=12948,ppid=4612,编号1
子进程开始执行>>> pid=1216,ppid=4612,编号0
子进程开始执行>>> pid=16320,ppid=4612,编号2
子进程开始执行>>> pid=14496,ppid=4612,编号3
子进程开始执行>>> pid=2176,ppid=4612,编号4
子进程终止>>> pid=1216,ppid=4612,编号0
子进程终止>>> pid=16320,ppid=4612,编号2
子进程终止>>> pid=12948,ppid=4612,编号1
子进程开始执行>>> pid=16320,ppid=4612,编号6
子进程开始执行>>> pid=1216,ppid=4612,编号5
子进程终止>>> pid=14496,ppid=4612,编号3
子进程终止>>> pid=2176,ppid=4612,编号4
子进程开始执行>>> pid=12948,ppid=4612,编号7
子进程开始执行>>> pid=14496,ppid=4612,编号8
子进程开始执行>>> pid=2176,ppid=4612,编号9
子进程终止>>> pid=1216,ppid=4612,编号5
子进程终止>>> pid=12948,ppid=4612,编号7
子进程终止>>> pid=14496,ppid=4612,编号8
子进程终止>>> pid=16320,ppid=4612,编号6
子进程终止>>> pid=2176,ppid=4612,编号9
主进程终止
'''

'''
同步执行结果
主进程开始执行>>> pid=14344
子进程开始执行>>> pid=13704,ppid=14344,编号0
子进程终止>>> pid=13704,ppid=14344,编号0
子进程开始执行>>> pid=8624,ppid=14344,编号1
子进程终止>>> pid=8624,ppid=14344,编号1
子进程开始执行>>> pid=10520,ppid=14344,编号2
子进程终止>>> pid=10520,ppid=14344,编号2
子进程开始执行>>> pid=5872,ppid=14344,编号3
子进程终止>>> pid=5872,ppid=14344,编号3
子进程开始执行>>> pid=4204,ppid=14344,编号4
子进程终止>>> pid=4204,ppid=14344,编号4
子进程开始执行>>> pid=13704,ppid=14344,编号5
子进程终止>>> pid=13704,ppid=14344,编号5
子进程开始执行>>> pid=8624,ppid=14344,编号6
子进程终止>>> pid=8624,ppid=14344,编号6
子进程开始执行>>> pid=10520,ppid=14344,编号7
子进程终止>>> pid=10520,ppid=14344,编号7
子进程开始执行>>> pid=5872,ppid=14344,编号8
子进程终止>>> pid=5872,ppid=14344,编号8
子进程开始执行>>> pid=4204,ppid=14344,编号9
子进程终止>>> pid=4204,ppid=14344,编号9
主进程终止
'''