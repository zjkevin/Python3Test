#扫描作业实体类
# -*- coding: UTF-8 -*-
#author zhangjie
#date 2016-05-31

from datetime import datetime
class job(object):
    """docstring for job"""
    def __init__(self):
        super(job, self).__init__()
        #扫描批次号，如果支持多线程或者分布式，批次号需要重构
        self.batch_number = "".join(str(datetime.now().timestamp()).split(".")[:-1])
        #当前扫描的邮箱
        self.current_scan_mailbox = None
        #完成扫描的邮箱
        self.scan_mail_done_list = []
        #有效邮件
        self.total_match = 0
        #无效邮件
        self.failed_match = 0
        #总邮件
        self.total = 0
        #各个扫描邮箱的扫描信息
        self.mailbox_scan_info_list = []
        #扫描邮箱列表
        self.scan_email_list = []

#单个邮箱的扫描信息
class mailbox_scan_info(object):
    """docstring for mailbox_scan_info"""
    def __init__(self):
        super(mailbox_scan_info, self).__init__()
        #邮箱地址
        self.address = ''
        #已扫描邮件的时间列表
        self.scan_time_list = []
        #有效邮件
        self.total_match = 0
        #无效邮件
        self.failed_match = 0
        #总邮件
        self.total = 0        
        
        