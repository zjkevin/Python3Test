#邮件扫描公共函数
# -*- coding: UTF-8 -*-
#author zhangjie
#date 2016-06-07
import yaml
from models import mail_box_entity


#得到扫描邮箱实体列表
def get_scan_mail_list(scan_eamil_file):
    scan_email_dict = {}
    with open(scan_eamil_file,'r') as f:
        scan_email_dict = yaml.load(f)
    scan_email_list = list(filter(lambda i:i["flag"] == 0, scan_email_dict["emails"]))
    __mb_list = [] 
    for i in scan_email_list: 
        mb = mail_box_entity.mailbox()
        mb.protocol = i["protocol"]
        mb.address = i["address"]
        mb.server = i["server"]
        mb.passwd = i["passwd"]
        __mb_list.append(mb)
    return __mb_list

# 把MyObj对象转换成dict类型的对象
def convert_to_builtin_type(obj):
    d = {}
    d.update(obj.__dict__)
    return d  

#写扫描的单条邮件记录
def write_scan_tmp(ae_obj,address,batch_number,index):
    tmp_file_path = os.path.join(os.path.abspath("."),"scantmp",address.replace("@","").replace(".",""),batch_number)
    if not os.path.exists(tmp_file_path):
        os.mkdir(tmp_file_path)
    tmp_file = os.path.join(tmp_file_path,index)
    j_s = json.dumps(ae_obj,default=convert_to_builtin_type)
    j_s = j_s.replace(r'\\u',r'\u')
    with codecs.open(tmp_file,'w','utf-8') as f:
        f.write(j_s)