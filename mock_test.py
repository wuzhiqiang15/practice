from unittest import mock
import os
import unittest

class Remove(object):
    def rmdir(self, path='C:\www'):
        r = os.rmdir(path)
        if r == None:
            return success
        else:
            return fail

    def exists_get_rmdir(self):
        return self.rmdir()

class MockTest(unittest.TestCase):
    def setUp(self):
        self.r = Remove()

    def tearDown(self):
        pass

    def test_success_rmdir(self):
        '''
        删除目录成功
        '''
        #print("rmdir修改前的内容:%s"% self.r.rmdir())
        succecc_path = mock.Mock(return_value="success")
        self.r.rmdir = succecc_path
        #print("赋值后的rmdir内容为：%s" %self.r.rmdir)
        self.assertEqual(self.r.exists_get_rmdir(), "success")

    def test_fail_rmdir(self):
        '''
        删除目录失败
        :return:
        '''
        fail_path = mock.Mock(return_value="fail")
        self.r.rmdir = fail_path
        self.assertEqual(self.r.exists_get_rmdir(), "fail")

if __name__ == "__main__":
    unittest.main(verbosity=2)