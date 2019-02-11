# 获取进程号(pid)和父进程号（ppid）

from multiprocessing import Process
import os

def info_test(title):
    print(title)
    print("module name is ", __name__)
    # 获取父进程的id
    print("父进程的ID为：", os.getppid())
    # 获取本身进程的id
    print("进程号为：", os.getpid())


def pid_test(name):
    info_test("main line")
    print("hello", name)

if __name__ == "__main__":
    info_test("main line")
    # 创建一个子进程（被创建后的进程是当前程序的子进程，所以它的父进程id = 当前进程的ID）
    p = Process(target=pid_test, args=("nash",))
    p.start()
    p.join()