# 多线程的使用

import time
import threading

def fun():
    print("start fun")
    time.sleep(4)
    print("end fun")

# 一个程序，对应一个进程，以这个"tereading_new_01.py"文件为例，当这个文件运行时，则会启动对应的进程
# 每个进程都有对应的主线程，当进程启动时，也会启动主线程
# 程序运行后，首先会输出这段内容
print("Main thread is running")

# 这里会去创建一个子线程，调用的是fun这个函数
t1 = threading.Thread(target=fun, args=() )
# 创建子线程后，必须用stast()方法，才能启动该子线程
# 这里用start()启动子线程后，会首先输出fun()函数中的“start fun”语句，然后子线程 sleep 4秒
t1.start()

# 主线程sleep 2 秒
time.sleep(2)
# 主线程休眠结束后，输出以下内容，然后主线程的运行就结束了
print("Main thread end")
# 当主线程结束后，子线程还处于sleep状态，当子线程sleep结束后，会输出fun()函数中的“end fun”命令