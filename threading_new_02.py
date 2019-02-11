# 守护线程的使用

import time
import threading

def fun():
    print("fun start")
    time.sleep(4)
    print("end fun")

print("main threading running")

t1 = threading.Thread(target=fun, args=() )
# 设置该子线程为守护线程
# 守护线程，会在主线程结束的时候，自动结束运行
t1.setDaemon(True)
t1.start()

time.sleep(2)
# 运行完下面这段代码后，主线程结束，此时，还处于sleep状态的守护线程也会随之结束运行，所以不会输出“end fun”这句话
print("Main thread is end now")
