'''
当使用dict，遇到key不在字典中时，会出现报错，这个时候就可以使用defaultdict类
defaultdict的作用是在于，当字典里的key不存在但被查找时，返回的不是KeyError而是一个默认值
defaultdict接受一个工厂函数作为参数，如下来构造
dict = defaultdict(factory_function)
这个factory_function可以是list，set，str等等，作用是当key不存在时，返回的是工厂函数的默认值：
比如list对应[ ]，str对应的是空字符串，set对应set()，int对应0
'''
from collections import defaultdict

# 要注意，defaultdict是一个类，所以这里相当于是实例化了4个defaultdict()的类对象
dict_1 = defaultdict(int)
dict_2 = defaultdict(set)
dict_3 = defaultdict(str)
dict_4 = defaultdict(list)

# 这里设置dict_1字典中，name的值为"nash"
dict_1['name'] = "nash"

# 接下来，分别查找各个dict中，age的值（由于前面没有给'age'赋值，所以aeg是不存在的，而defaultdict会使用默认的值给age赋值）
print(dict_1['age'])
print(dict_2['age'])
print(dict_3['age'])
print(dict_4['age'])
