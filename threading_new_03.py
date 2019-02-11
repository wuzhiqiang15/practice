# 多线程的属性

import time
import threading

def loop1():
    # time.ctime()，得到当前时间
    print("Start loop 1 at :", time.ctime())
    time.sleep(4)
    print("End loop 1 at :", time.ctime())

def loop2():
    print("Start loop 2 at :", time.ctime())
    time.sleep(2)
    print("End loop 2 at :", time.ctime())

def loop3():
    print("Start loop 3 at :", time.ctime())
    time.sleep(5)
    print("End loop 3 at :", time.ctime())

def main():
    print("Starting at :", time.ctime())
    # 生成子线程
    t1 = threading.Thread(target=loop1, args=())
    # setName是给子线程设置一个名字
    t1.setName("THR_1")
    t1.start()

    t2 = threading.Thread(target=loop2, args=() )
    t2.setName("THR_2")
    t2.start()

    t3 = threading.Thread(target=loop3, args=() )
    t3.setName("THR_3")
    t3.start()

    # 主线程sleep 3秒
    time.sleep(3)
    # threading.enumerate() 获取正在运行的子程序，即子线程1和子线程3（此时子线程2已经结束运行了）
    for thr in threading.enumerate():
        # getName 能够获取到线程的名称
        print("正在运行的线程名字是：{0}".format(thr.getName()))

    print("正在运行的子线程数量为：{0}".format(threading.activeCount()))

    print("ALL done at:", time.ctime())

if __name__ == "__main__":
    main()
    #while True:
    #    time.sleep(10)