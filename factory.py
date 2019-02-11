# 简单工厂模式
#人类，通过调用工厂类，去使用不同的斧头进行工作
class Person(object):
    def __init__(self,name):
        self.name = name

    def work(self,axe_type):
        print('%s开始工作' % self.name)
        #这里直接调用工厂类中的方法，来实现通过对象传参调用不同的斧头类
        axe = Factory.create_axe(axe_type)
        axe.cut_tree()

#原始的斧头类，拥有砍树的方法
class Axe(object):
    def cut_tree(self):
        print('用斧头砍树')

#继承斧头类的子类
class StoneAxe(Axe):
    def cut_tree(self):
        print('使用石斧砍树')

#继承斧头类的子类
class SteelAxe(Axe):
    def cut_tree(self):
        print('使用金属斧头砍树')

# 简单工程类，需要定义一个静态方法
class Factory(object):
    @staticmethod
    def create_axe(type):
        if type == 'stone':
            return StoneAxe()
        elif type == "steel":
            return SteelAxe()
        else:
            print("类型错误")

P = Person('zs')
P.work('steel')