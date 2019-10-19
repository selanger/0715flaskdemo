import unittest

class MyTest(unittest.TestCase):

    def setUp(self):
        """
        在测试执行之前执行，用来加载  准备测试参数
        :return:
        """
        self.a = 10
        self.b = 11

    ## 需要写测试代码
    ## 测试方法必须的要求     test_   开头
    def test_demo(self):
        self.assertEquals(self.a,self.b,msg="a 和 b 不相等")
    def test_demo_has_id(self):
        pass

    def tearDown(self):
        """
        在测试之后执行，用于回收测试环境
        :return:
        """
        pass


if __name__ == '__main__':
    unittest.main()  ## 启动测试