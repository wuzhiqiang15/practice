# 进程池 ,可以用来启动大量的子进程

from multiprocessing import Pool
import os,time,random

def long_time_task(name):
    print('Run task %s(%s)...' % (name, os.getpid()))
    start = time.time()  # 获取当前时间，并将其赋值给start
    # time.sleep()函数可以推迟调用线程的运行时间，具体时间由传入的参数决定
    time.sleep(random.random()*3)
    end =time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__ == '__main__':
    print('Parent process %s.' %os.getpid())
    # 这里是设置线程池的数量，控制最高可并发线程数
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()  # 调用close()方法后就不能继续添加新的进程了
    p.join()  # 对Pool对象调用join()方法必须先调用close()方法
    print('All subprocesses done')