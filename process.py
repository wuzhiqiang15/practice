# 多进程在windows上的运用
# multiprocessing模块中提供了一个Process类来代表一个进程对象
from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__ == '__main__':
    print('Parent process %s.' % os.getppid())
    # 在这里调用导入的Process类，target和args都是调用Process类时传入的属性
    p = Process(target= run_proc, args=('test',))
    print('Child process will start')
    # 启动子进程，调用start()方法后，会运行target指定的函数（比如这里会运行run_proc中的代码）
    p.start()
    p.join()  # 等待父进程结束
    print('Child process end')