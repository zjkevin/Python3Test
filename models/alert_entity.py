#告警信息实体类
# -*- coding: UTF-8 -*-
#author zhangjie
#date 2016-05-24

class alert(object):
    """docstring for alert"""
    def __init__(self):
        super(alert, self).__init__()
        #邮件主题
        self.title = ''
        #告警等级
        self.level = ''
        #事件时间
        self.event_time = ''
        #主机
        self.host = ''
        #主机角色
        self.hostrole = ''
        #主机组
        self.hostgroup = ''
        #状态
        self.status = ''
        #节点
        self.node = ''
        #事件代码
        self.event_code = ''
        #告警代码
        self.alert_code = ''
        #数据
        self.data = ''
        #邮件时间
        self.email_time = ''


		