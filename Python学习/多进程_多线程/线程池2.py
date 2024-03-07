# -*- coding: utf-8 -*-
from multiprocessing.pool import ThreadPool
import time

pool = ThreadPool(2)  # 创建两个线程


def funa(x, y):
    print('%s好好学习' % x)
    time.sleep(3)
    print('天天向上')


def funb(x, y):
    print('%shello' % x)
    time.sleep(3)
    print('world')


# 我们这就是有一个线程池，里面有两个等待处理任务的线程，然后这两个函数就是两个任务，
# 线程池里一个线程处理一个，所以会同时输出！如果多于两个任务就会执行等待sleep

pool.apply_async(funa, args=('我们要————', 2))  # 将任务添加到线程池
pool.apply_async(funb, args=('大家要————', 4))

pool.close()  # close之后则无法向线程池提交任务

# 内置线程池，自带守护线程，主线程结束，子线程也跟着结束
# 所以需要加阻塞，否则主线程一结束，子线程也跟着结束，无输出
pool.join()  # 在join之前可使用终止线程，直接终止线程pool：  pool.terminate()

print('这是程序的最后一行，执行到这里，主线程结束')