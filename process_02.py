from multiprocessing import Process
import time,random,os

class Pro(Process):       # 新增一个Pro类，继承Process
    def __init__(self, name):
        self.name = name
     # 这里因为对父类的__init__()方法重写了，但是又缺少父类的一些核心属性，所以要调用父类的__init__方法
        super().__init__()

# 对父类Process类的run()方法进行重写
# 我们运行进程时，如果没有指定target参数（如下P= Pro('nash')），那么将运行这个run()方法
    def run(self):
        print('%s is start' %self.name)
        time.sleep(random.randrange(1,3))
        print('%s is run end' %self.name)

if __name__ =='__main__':
        P = Pro('nash')
        P.start()
        P.join(1)
        print('开始执行')