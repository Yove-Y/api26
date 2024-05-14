#用于建立smtp链接
import smtplib
#邮件需要专门的MIME格式
from email.mime.text import MIMEText
#支持附件
from email.mime.multipart import MIMEMultipart
#用于使用中文邮件主题
from email.header import Header
#读取report的内容  放到变量email_body中
with open("../report/report.html", encoding='utf-8')as f:
    email_body=f.read()
#plain指普通文本格式邮件内容
#msg=MIMEText('想不出来内容','plain',"utf-8")
msg=MIMEMultipart()
msg.attach(MIMEText(email_body,'html','utf-8'))
#发件人邮箱
msg['From']='13872799364@163.com'
# 收件人邮箱
msg["To"]='13872799364@163.com'
#邮件的标题
msg["Suject"]=Header('接口测试报告','utf-8')

#上传附件
#构造附件1，传送当前目录下的report.html文件
att1=MIMEText(open('../report/report.html', 'rb').read(), 'base64', 'utf-8')  #二进制格式打开
att1["Content-type"]='application/octet-stream'
att1["Content-Disposition"]='attachment;fileneme="report.html"'  #filename附件显示的名字
msg.attach(att1)
#建立连接
smtp=smtplib.SMTP_SSL('smtp.163.com')
#登录邮箱
smtp.login('13872799364@163.com','LKJCZQANQKUTKADZ')
#发送邮寄
smtp.sendmail('13872799364@163.com','13872799364@163.com',msg.as_string())
smtp.quit() 20031218@Ylh