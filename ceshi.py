#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 20:31:36 2022

@author: carson
"""


#coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
 
 
# --------------------------------------------配置信息开始
 
mail_host = "smtp.163.com"             # 设置服务器(如果是qq邮箱，将163换成qq)
mail_user = 'lee_daowei@163.com'   # 用户名
mail_pass = 'ofhakvdvbpemqiwp'         # 口令
 
username = 'lee_daowei@163.com'   # 发件人名称
 
getusername = 'lee_daowei@qq.com'        # 收件人名称
getmail =['lee_daowei@qq.com']            # 收件人邮箱
 
context = '这里填正文'                # 内容
title = '这里填标题'                  # 标题
 

def email():
    sender = True
    try:
        massage= MIMEText(context, 'plain', 'utf-8')     # 加入正文内容
        massage['From'] = Header(username, 'utf-8')      # 加入发件人名称
        massage['To'] = Header(getusername, 'utf-8')      # 加入收件人名称
        massage['Subject'] = Header(title, 'utf-8')     # 加入标题
 
        server = smtplib.SMTP_SSL()                         # 获取服务 25端口不需要加 _SSL
        server.connect(mail_host, 465)                   # 链接服务  25和465都为SMTP端口号
        server.login(mail_user, mail_pass)              # 登录服务
        server.sendmail(mail_user, getmail, massage.as_string())      # 开始发送
 
        server.close()                                  #关闭服务
 
    except smtplib.SMTPException :
        sender = False
    return sender

sender = email()
if sender:
    print("邮件发送成功 ...")
else:
    print("邮件发送失败 ...")