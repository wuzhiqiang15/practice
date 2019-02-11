# 工厂方法模式。跟简单工厂模式不同，工厂方法没有用静态方法，而是用到了工厂类的继承
#人类，通过调用工厂类，去使用不同的斧头进行工作
class Person(object):
    def __init__(self,name):
        self.name = name

    def work(self):
        print('%s开始工作' % self.name)
        #这里直接调用工厂类中的方法，来实现通过对象传参调用不同的斧头类
        #factory = Stone_Axe_Factory()
        #axe = factory.create_axe()
        axe = Stell_Axe_Factory().create_axe()
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

# 工厂方法模式，先定义一个工厂方法，然后定义不同的之类继承它
class Factory(object):
    def create_axe(self):
        pass

# 继承工厂方法，每个子类返回不同的内容
class Stone_Axe_Factory(Factory):
    def create_axe(self):
        return StoneAxe()

class Stell_Axe_Factory(Factory):
    def create_axe(self):
        return SteelAxe()

P = Person('zs')
P.work()