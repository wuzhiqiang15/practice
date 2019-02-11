# 导入单元测试模块
import unittest
# 导入需要进行单元测试的类
from unit_test1 import Dict

# 创建单元测试类，必须继承unittest.TestCase
class TestDict(unittest.TestCase):
    # setUp()和tearDown() 每调用一个测试方法的前后都会分别被执行
    def setUp(self):
        print('setup---01')
    def tearDown(self):
        print('tearDown---01')

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

    def preson(self):  # 不是test开头，不会被执行
        print('不以test开头的方法在unittest中不被认为是测试方法，测试的时候不会被执行')

# 运行单元测试（调用unittest.main()方法）
if __name__ == '__main__':
    unittest.main()