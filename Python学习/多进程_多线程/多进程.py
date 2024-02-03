import time
import multiprocessing
import os


def drink(num, name):
    print("喝汤的进程ID:", os.getpid())
    print("喝汤的主进程ID:", os.getppid())
    for i in range(num):
        print(name + "喝一口……")
        # time.sleep(1)
        for j in range(10000):
            pp=0


def eat(num, name):
    print("吃饭的进程ID:", os.getpid())
    print("吃饭的主进程ID:", os.getppid())
    for i in range(num):
        print(name + "吃一口……")
        # time.sleep(1)
        for j in range(10000):
            pp=0





if __name__ == '__main__':
    # target:指定函数名
    # args:使用元组方式给指定任务传参
    # kwargs:使用字典方式给指定任务传参
    # drink_process = multiprocessing.Process(target=drink)
    # eat_process = multiprocessing.Process(target=eat)
    # eat_process = multiprocessing.Process(target=eat, args=(3, "giao"))
    run_num = 100000
    eat_process0 = multiprocessing.Process(target=eat, kwargs={"num": run_num, "name": "giao"})
    eat_process1 = multiprocessing.Process(target=eat, kwargs={"num": run_num, "name": "giao"})
    eat_process2 = multiprocessing.Process(target=eat, kwargs={"num": run_num, "name": "giao"})
    eat_process3 = multiprocessing.Process(target=eat, kwargs={"num": run_num, "name": "giao"})
    eat_process4 = multiprocessing.Process(target=eat, kwargs={"num": run_num, "name": "giao"})
    eat_process5 = multiprocessing.Process(target=eat, kwargs={"num": run_num, "name": "giao"})
    eat_process6 = multiprocessing.Process(target=eat, kwargs={"num": run_num, "name": "giao"})
    drink_process = multiprocessing.Process(target=drink, kwargs={"num": run_num, "name": "giao"})
    print("主进程ID:", os.getpid())
    # 设置进程守护
    # eat_process0.daemon = True
    # eat_process1.daemon = True
    # eat_process2.daemon = True
    # eat_process3.daemon = True
    # eat_process4.daemon = True
    # eat_process5.daemon = True
    # eat_process6.daemon = True
    # drink_process.daemon = True
    drink_process.start()
    eat_process0.start()
    eat_process1.start()
    eat_process2.start()
    eat_process3.start()
    eat_process4.start()
    eat_process5.start()
    eat_process6.start()

    time.sleep(1)
    print("我吃饱了……")
