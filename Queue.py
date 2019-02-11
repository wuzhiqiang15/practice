# 使用“队列”进行进程之间的通信

from multiprocessing import Queue, Process
import os, time, random

# 写数据的进程
def write(q1):
    print('写数据的子进程，进程号:%s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('将 %s 放入队列中' % value)
        # put()方法将数据插入到Queue中
        q1.put(value)
        time.sleep(random.random())

# 读取数据的进程
def read(q2):
    print('读取数据的子进程，进程号:%s' % os.getpid())
    while True:
        # 这里实现了不同进程中的通信，write进程使用put()方法把数据写入Queue，然后read进程使用get()方法读取Queue中的数据
        value_1 = q2.get()  # get()方法从Queue中读取并删除一个数据
        print('从队列中获取了数据：%s' % value_1)

if __name__ == "__main__":
    # 父进程创建Queue，并传给各个子进程，这里设置了队列中最大并发数为3
    q = Queue(3)
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入：
    pw.start()
    # 启动子进程pr，读取：
    pr.start()
    # 等待 pw进程结束：
    pw.join()
    # pr 进程里是死循环，无法等待其结束，只能强行终止
    pr.terminate()