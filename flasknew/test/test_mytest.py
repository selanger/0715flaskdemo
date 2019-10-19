import unittest
## 导入 create这个工厂方法
from app import Create
from settings import TestConfig
import json


class TestConfigTest(TestConfig):
    TESTING = True


class TestMyTest(unittest.TestCase):
    def setUp(self):
        self.app = Create(TestConfigTest)
        self.client = self.app.test_client()   ##  属于flask 提供的测试方法

    def test_has_id(self):
        # 给 mytest 这个路由  发出get请求  传递id参数
        # 拿到返回值
        # 判断返回值是否满足我们的预期
        #发送get请求    使用urllib和requests发送请求，必须需要flask服务开启的
        ## 第二种 使用flask提供的方法进行get，post，put，delete请求，不需要开启flask服务
        resp = self.client.get("/mytest/?id=1")
        ##  首先应该看一下  返回的状态码   200
        self.assertEquals(resp.status_code,200)
        ## 判断返回值 是否符合预期
        result_data =resp.data   ### 返回的 结果
        result_data = result_data.decode()
        data = json.loads(result_data)  ## 反序列化
        ## 判断返回值中时候有data
        self.assertIn("data",data)    ## 判断 data 是否在返回值中包含
        ## 判断返回值中 code 是否为 10000
        self.assertEquals(data["code"],10001)

    def test_no_id(self):
        pass



    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()

