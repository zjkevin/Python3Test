#单封嵌套的内容
# -*- coding: UTF-8 -*-
#author zhangjie
#date 2016-06-08

class email_part_enty(object):
    """docstring for alert"""
    def __init__(self):
        super(email_part_enty, self).__init__()
        #邮件内容
        self.content = ''
        #content-transfer-encoding
        self.cte = ''
        #Content-Type
        self.ct = ''
        #charset
        self.charset = ''