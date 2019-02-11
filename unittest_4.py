# 手工加载批量测试用例

import unittest

class TestOne(unittest.TestCase):
    def setUp(self):
        print('\ncase before')
        pass

    def test_add(self):
        '''test add method'''
        print('add.......')
        a = 3+4
        b = 7
        self.assertEqual(a, b)

    def test_sub(self):
        '''test sub method'''
        print('test_sub...')
        a = 10 - 5
        b = 5
        self.assertEqual(a, b)

    def tearDown(self):
        print('case after')
        pass


if __name__ == '__main__':
    # 1、构造用例集
    suite = unittest.TestSuite()

    # 2、用例执行顺序是按加载的顺序（以本次为例，先执行test_sub，再执行test_add）
    suite.addTest(TestOne("test_sub"))
    suite.addTest(TestOne("test_add"))

    # 3、实例化runner类
    runner = unittest.TextTestRunner()

    # 4、执行测试(调用runner类的run方法，参数是测试用例集)
    runner.run(suite)