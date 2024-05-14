import json
import requests

from lib import read_excel
from lib.db import *



class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.r = read_excel.readexcel()
        cls.l = cls.r.excel_to_list("test_user_data.xlsx", "test_user_reg")

    def test_reg_ok(self):
        reg1=self.r.get_test_data(self.l,"reg_ok")
        # print(reg1)
        url=reg1.get("url")
        # 获取是字符串格式

        args=reg1.get("args")
        res=reg1.get("expect_res")
        # 将字符串转化字典
        a=json.loads(args)
        # 提取提交参数中的username值
        name=a.get("userName")

        # 在数据库中作比对，如果数据库中有，就删除
        if check_user(name):
            del_user(name)
        r=requests.post(url,json=a)
        logging.info("测试用例".format('test_reg_ok'))
        logging.info("url".format(url))
        logging.info("请求参数".format(args))
        logging.info("预期结果".format(res))
        logging.info("实际结果：{}".format(r.text))
        self.assertIn(res,r.text)
        # 测试完成后，还原数据
        del_user(name)

    def test_reg_err(self):
        reg1=self.r.get_test_data(self.l,"reg_err")
        # print(reg1)
        url=reg1.get("url")
        # 获取字符串格式
        args=reg1.get("args")
        res=reg1.get("expect_res")
        # 将字符串转化字典
        a=json.loads(args)

        r=requests.post(url,json=a)
        logging.info("测试用例".format('test_reg_err'))
        logging.info("url".format(url))
        logging.info("请求参数".format(args))
        logging.info("预期结果".format(res))
        logging.info("实际结果：{}".format(r.text))

        self.assertIn(res,r.text)




if __name__ == '__main__':
    unittest.main()
