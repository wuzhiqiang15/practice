import os
# 案例说明：os.path.dirname(__file__)和os.path.abspath(__file__)的区别

# 返回当前py脚本文件的路径(例如，这里应该返回  E:/PyCharm/Python_code)
a = os.path.dirname(__file__)
# 返回该py文件所属路径的上一层的目录（例如，这里应该返回 E:/PyCharm）
b = os.path.dirname(os.path.dirname(__file__))

# 返回当前py脚本文件的绝对路径（与os.path.dirname不同，这里会返回路径中，会带上py文件的名称，如 E:\PyCharm\Python_code\osPathDir_01.py）
c = os.path.abspath(__file__)
# 返回当前py文件所处的路径，和os.path.dirname(__file__)返回内容相同
d = os.path.dirname(os.path.abspath(__file__))

print('a at:', a)
print('b at :', b)
print('c at :', c)
print('d at :', d)