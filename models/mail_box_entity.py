#邮箱实体类
# -*- coding: UTF-8 -*-
#author zhangjie
#date 2016-06-01

class mailbox(object):
    """docstring for mailbox"""
    def __init__(self):
        super(mailbox, self).__init__()
        #处理协议，目前支持pop3和imap
        self.protocol = ''
        #邮箱地址
        self.address = ''
        #邮箱服务器
        self.server = ''
        #邮箱密码
        self.passwd = ''