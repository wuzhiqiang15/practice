# 单个测试用例执行
import unittest
# 继承unittest.TestCase的类
class TestOne(unittest.TestCase):
    # 配置环境：进行测试前的初始化工作
    def setUp(self):
        print('\n cases before')
        pass

    # 定义测试用例，名字以“test”开头
    def test_add(self):
        ''' test add method '''
        print('this is add.....')
        a = 3+4
        b = 7
        # 定义assert断言，判断测试结果
        self.assertEqual(a, b)

    def test_sub(self):
        ''' test sub method '''
        print('this is sub....')
        a = 10 - 5
        b =4
        self.assertNotEqual(a, b)

    # 清理环境
    def tearDown(self):
        print('case after')
        pass

# unittest.main()方法会搜索该模块下所有以test开头的测试用例方法，并自动执行它们
if __name__ == '__main__':
    unittest.main()