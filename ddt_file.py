import unittest
import method
from ddt import ddt,file_data

#装饰ddt
@ddt
class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.run=method.RunMain()

    #导入file_data()获取json中的数据,在test_something测试函数中接受
    @file_data("test_data_list.json")
    def test_something(self,message):
        name, method, url, data, assertion, value=message[0],message[1],message[2],message[3],message[4],message[5]

        print("测试接口为：%s"%name)

        rep=self.run.run_main(url,method,data)
        print(rep)
        self.assertEqual(rep['successful'],1,'测试通过')



if __name__ == '__main__':
    unittest.main()
