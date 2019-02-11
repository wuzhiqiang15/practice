from multiprocessing import Process
import os,time,random

def fun_test(name):
    print('子进程运行中，子进程号：%s，二号：%s，父进程号：%s' % (os.getpid(),os.getpid(), os.getppid()))
#print(fun_test('tom'))

P1 = Process(target=fun_test,args=('tom',))
P2 = Process(target=fun_test,args=('tom',))

if __name__ == '__main__':
    P1.start()
    P2.start()

    '''
    print(P1.name)
    print(P1.pid)
    P1.join(2)
    '''