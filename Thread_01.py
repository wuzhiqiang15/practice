# 多线程的使用
import threading,time

# 新线程执行的代码
def loop():
    # threading.current_thread().name 方法会返回当前线程的实例名称
    # 这里的线程名称，是创建线程时，传入的name参数的值
    print('线程 %s 开始运行' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('线程 %s 》》》 %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('线程 %s 运行结束' % threading.current_thread().name)

# 程序首先会执行这一步，这里的线程名是主线程，即“MainThread”
print('主线程 %s 正在急速运行当中哦' % threading.current_thread().name)

# 创建新线程
t = threading.Thread(target=loop, name='newThread')  # 这里如果不传name，则线程名默认为“Thread-1”
t.start()  # 启动线程
t.join()   # 结束线程
print('主线程 %s 结束了哦' % threading.current_thread().name)