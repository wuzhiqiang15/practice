# 多进程

import multiprocessing
from time import sleep,ctime

class ClockProcess(multiprocessing.Process):
    # 重写父类的__init__()方法
    def __init__(self, interval):
        super().__init__()
        self.interval = interval

    # 重写父类的 run()方法
    def run(self):
        while True:
            print("The time is {0}".format(ctime()))
            sleep(self.interval)

if __name__ == "__main__":
    p = ClockProcess(3)
    p.start()

    while True:
        print("sleeping......")
        sleep(1)