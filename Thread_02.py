# 使用Lock()给线程上锁
import time,threading

balance = 0
# 创建一个锁
lock = threading.Lock()

def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n1):
    for i in range(100000):
        # 获取锁，将当前线程锁住
        lock.acquire()
        try:
            change_it(n1)
        except Exception as ex:
            print('捕获到错误:%s' % ex)
        finally:
            # 释放锁。获得锁的线程一定要释放锁，不然就会变成死线程
            lock.release()

t1 = threading.Thread(target=run_thread, args=(5, ))
t2 = threading.Thread(target=run_thread, args=(8, ))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)