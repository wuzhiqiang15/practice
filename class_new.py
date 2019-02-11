# __new__()方法的使用说明

class User(object):

    def __init__(self,username,password):
        self.username = username
        self.password = password
        print('对象已经构建好了，由python解释器自动回调__init__方法，对象初始化')

# __new__()方法是当对象构建的时候由解释器自动回调的方法，该方法必须返回当前类的对象
    def __new__(cls,username,password):
        print('User类的对象开始构建')
        return object.__new__(cls)   # 调用父类object类的__new__()方法，返回当前类的对象

    def __str__(self):
        return '用户名是：%s，密码是：%s' % (self.username, self.password)

u1 = User('wuzhiqiang','123456789')
print(u1)