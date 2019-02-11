class Person():

    def __init__(self,name,age,heghit):
        self.name = name
        self.age = age
        self.heghit = heghit

    def __str__(self):
        return ('名字是：%s，年龄是：%s，身高是：%scm' % (self.name, self.age, self.heghit))

    def print_init(self):
        print('名字是：%s，年龄是：%s' %(self.name, self.age))

p1 = Person('nash',31,192)
#p1.name = 'ww'
#p1.age = 22

p1.print_init()

print(p1)