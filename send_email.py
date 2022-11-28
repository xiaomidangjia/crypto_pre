# -*- coding:utf-8 -*-
"""
发邮件的类
注意：端口用465，登录方法用SMTP_SSL
smtplib.SMTP_SSL('smtp.mxhichina.com', 465)
"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.header import Header
from email.mime.image import MIMEImage
import datetime
from .logger_config import logger


class SendEmail(object):
    def __init__(self, smtp_host, smtp_port, smtp_user, smtp_pass, receivers):
        self.mail_host = smtp_host
        self.mail_port = smtp_port
        self.mail_user = smtp_user
        self.mail_pass = smtp_pass
        self.receivers = receivers
        self.msg = MIMEMultipart('mixed')
    
    # 重新设置收件人列表
    def reset_receivers(self, to_list):
        self.receivers = to_list

    # 添加正文内容 plain格式
    def attach_plain_content(self, text):
        self.msg.attach(MIMEText(text, 'plain', 'utf-8'))

    # 添加正文内容 html格式
    def attach_html_content(self, text):
        self.msg.attach(MIMEText(text, 'html', 'utf-8'))

    # 添加附件
    def attach_attachment(self, content, file_name):
        try:
            file_msg = MIMEApplication(content)
            file_msg.add_header('Content-Disposition', 'attachment', filename=Header(file_name, 'utf-8').encode())
            self.msg.attach(file_msg)
        except Exception as e:
            logger.error(e)

    # 读取本地文件添加附件
    def attach_attachment_from_file(self, file_path, file_name):
        try:
            mail_body = open(file_path, 'rb').read()
            file_msg = MIMEText(mail_body, 'html', 'utf-8')
            file_msg.add_header("Content-Disposition", "attachment", filename=("utf-8", "", file_name))
            self.msg.attach(file_msg)
        except Exception as e:
            logger.error(e)

    # 添加图片
    # 使用这个函数添加完图片后，还需把图片加到正文中content+= '<img src="cid:fig_name">'
    def attach_fig(self, fig_path, fig_name):
        image = MIMEImage(open(fig_path, 'rb').read())
        image.add_header('Content-ID', '<{}>'.format(fig_name))
        self.msg.attach(image)
    
    # 发送邮件，设置一下邮件的主题 subject
    def send_email(self, subject):
        self.msg['Subject'] = subject
        self.msg['From'] = self.mail_user
        self.msg['To'] = ";".join(self.receivers)
        try:
            s = smtplib.SMTP_SSL(self.mail_host, self.mail_port)
            s.login(self.mail_user, self.mail_pass)
            s.sendmail(self.mail_user, self.receivers, self.msg.as_string())
            s.close()
            logger.info("邮件发送成功，Subject:{}, From: {}, TO: {}".format( self.msg['Subject'], self.msg['From'], self.msg['To']))
        except Exception as e:
            logger.error(e)


if __name__ == "__main__":
    mail_config = {
      "smtp_host": 'smtp.mxhichina.com',
      "smtp_port": 465,
      "smtp_user": "***@***.com",
      "smtp_pass": "abcd@1234",
      "receivers": ['user@***.com'],
    }
    mail = SendEmail(**mail_config)
    mail.attach_plain_content("oooool")
    mail.send_email("hello")