#单封邮件的实体类
# -*- coding: UTF-8 -*-
#author zhangjie
#date 2016-06-02

class email_enty(object):
    """docstring for alert"""
    def __init__(self):
        super(email_enty, self).__init__()
        #邮件时间
        self.email_time = ''
        #邮箱地址
        self.address = ''
        self.contents = []
        #邮件内容
        self.content = ''
        #邮件发件人信息
        self.from_str =''
        #邮件收件人信息
        self.to = ''
        #邮件主题
        self.subject = ''
        #邮件编码
        #content-transfer-encoding
        self.cte = ''