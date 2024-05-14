import logging
import os
from optparse import OptionParser



#项目路径
prj_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path=os.path.join(prj_path,"data")
test_path=os.path.join(prj_path,"test")
log_file=os.path.join(prj_path,'log',"log.txt")
report_file=os.path.join(prj_path, 'report',"report.html")
# #log文件配置
logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',
    datefmt='%Y-%m-%d %H:%H:%S', #日期格式
    filename='log.txt', #日志输出格式
    # encoding='utf-8',
    filemode='a'
)
#数据库配置
db_host='192.168.55.45'
db_port=3306
db_user='root'
db_passwd='root'
db='xzs'

#邮件配置
smtp_server='smtp.163.com'
smtp_user='13872799364@163.com'
smtp_password='LKJCZQANQKUTKADZ'
sender=smtp_user
receiver='13872799364@163.com'
subject='接口测试报告'




# 命令行参数解析
parser=OptionParser()
parser.add_option("--collect_only",action="store_true",dest="collect_only",help="测试用例名称")
parser.add_option("--makesuite-tag",action="store_true",dest="makesuite-tag",help="根据标签生成测试套件")
parser.add_option("--rerun_fails",action="store_true",dest="rerun_fails",help="重新运行失败用例")
#生效参数
(optparse,args)=parser.parse_args()

if __name__ == '__main__':
    logging.info("接口测试")parser                                                                                                                                                                                                                                                                                                            