# 多线程，锁的使用
import threading

sum = 0
loopsum = 10000

# 生成一个Lock的实例
lock = threading.Lock()

def myAdd():
    global sum, loopsum
    for i in range(1, loopsum):
        # 添加锁
        lock.acquire()
        sum = sum + 1
        # 释放锁
        lock.release()

def myMinu():
    global sum, loopsum
    for i in range(1, loopsum):
        # 添加锁
        lock.acquire()
        sum = sum - 1
        # 释放锁
        lock.release()

if __name__ == '__main__':
    print("Starting ...{0}".format(sum))

    t1 = threading.Thread(target=myAdd, args=())
    t2 = threading.Thread(target=myMinu, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done....{0}".format(sum))