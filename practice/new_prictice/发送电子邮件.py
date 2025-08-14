'''send mail'''

from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = '1525996190@qq.com'
EMAIL_HOST_PASSWORD = 'hofeqkcwpzdzieig'


def send_mail(from_user,to_user,subject,content):
    # 创建邮件主题对象
    eml = MIMEMultipart()
    eml['From'] = from_user
    eml['To'] = to_user
    eml['Subject'] = subject

    # 添加邮件正文
    eml.attach(MIMEText(content,'plain'))

    #连接邮件服务器
    smtp_obj = smtplib.SMTP_SSL(EMAIL_HOST,EMAIL_PORT)
    # 登录邮件服务器
    smtp_obj.login(EMAIL_HOST_USER,EMAIL_HOST_PASSWORD)
    # 发送邮件
    smtp_obj.sendmail(from_user,to_user,eml.as_string())
    smtp_obj.quit()

def main():
    from_user = EMAIL_HOST_USER
    to_user = 'yushanshan@sensorsdata.cn'
    subject = Header('小玉米', 'utf-8')
    content = '要上学喽'
    send_mail(from_user,to_user,subject,content)

if __name__ == '__main__':
    main()




