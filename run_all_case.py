# 运行指定路径下的case，并生成HTML测试报告
import unittest
import os
import time
import HTMLTestRunner

# 用例路径 (获取当前项目路径作为测试用例路径)
case_path = os.path.join(os.getcwd())

# 测试报告存放路径（在当前项目目录下的report文件夹）
report_path = os.path.join(os.getcwd(), 'report')
print(report_path)

def all_case():
    discover = unittest.defaultTestLoader.discover(case_path, pattern='test*.py', top_level_dir=None)

    print('测试用例文件为：', discover, '\n')
    return discover

if __name__ == '__main__':
    # 获取当前时间，便于下面使用
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

    # 2、html报告文件路径
    report_abspath = os.path.join(report_path, "result_" + "now" + ".html")

    # 3、打开一个文件，将result写入此文件中
    fp = open(report_abspath, "wb")

    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'接口自动化测试报告,测试结果如下：', description=u'用例执行情况：')

    # 4、调用 add_case() 函数返回值
    runner.run(all_case())
    fp.close()