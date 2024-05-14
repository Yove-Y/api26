import unittest,requests,json,sys,ast
from lib.case_log import *
from lib.read_excel import *
from config.config import *




class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpclass(cls):
        if cls.__name__=='BaseCase':
            cls.data_case=readexcel.excel_to_list(data_file,cls.__name__)

    def get_case_data(self,case_name):
        return readexcel.get_test_data(self.data_list,case_name)

    def dend_request(self):
        case_data=self.get_case_data(case_name)
        url=case_data['url']
        method=case_data['method']
        header=case_data['header']
        args=case_data['args']
        data-type=case_data['date_type']
        expect-res=case_data['expect_res']
        if mathod.upper()=='GET':
            response=requests.get(url,header=haeders,parms=args)

        elif data_type='json':

            data=json.dump(args)
            response=requests.request(method,url,headers=haeders,data=data)
            self.assertEqual(expect_res,response.text)
        elif data_type=='from':
            reponse=requests.request(method,url,headers=headers,data=args)
            self.assertIn(expect_res,reponse.text)
            self.assertIn()

if __name__ == '__main__':
    unittest.main()
