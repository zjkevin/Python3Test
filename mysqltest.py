
sql_select_one_str = "SELECT id,content,add_time FROM `production-opvis3`.opvis_alerts_alertmail limit %s,%s;"
sql_select_one_str1 = "SELECT id,content,add_time FROM `production-opvis3`.opvis_alerts_alertmail where id > %s and time_delta is null limit 100"
#sql_select_one_str1 = "SELECT id,content,add_time FROM `production-opvis3`.opvis_alerts_alertmail where id = 17012"

sql_update_str =  "UPDATE `production-opvis3`.`opvis_alerts_alertmail` SET `email_time` = %s, `time_delta` = %s WHERE `id` = %s;"

from email.parser import Parser
import re
from datetime import datetime
from models import email_entity
from models import alert_entity
from dismantle import dismantle_v1 as dm

_CHARSET = 'utf-8'

#邮件内容得到时间
def ac(content):
    lines = re.split("\r\n|\r|\n",content)
    lines = list(filter(lambda s: s and s.strip(), lines))
    lines = [bytes(x, encoding = "utf8") for x in lines]
    msg_content = b'\r\n'.join(lines).decode(_CHARSET)
    #print(msg_content)
    # 稍后解析出邮件:_CHARSET = 'utf-8'
    msg = Parser().parsestr(msg_content)
    __em = email_entity.email_enty()
    __ae_obj = alert_entity.alert()
    __em = dm.parse(msg,__em)
    print(type(__em))
    email_time_str = None
    print("----------------1--------------------")
    if not __em == None:
        for e in __em.contents:
            print("----------------2--------------------")
            __ae_obj = dm.dismantle(e)
            if __ae_obj:
                print("----------------3--------------------")
                email_time_str =  __ae_obj.event_time
    print("----------------4--------------------")
    if email_time_str == '' or email_time_str == None:
        email_time_str = dm.parse_x(msg.__str__())
    print("----------------5--------------------")
    print(email_time_str)
    return email_time_str

def update_time_delta():
    conn = mysql.connector.connect(host='192.168.13.186', user='converger', password='converger', database='production-opvis3')
#cursor = conn.cursor()
# 执行语句
#cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
#cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
#cursor.rowcount
#1
# 提交事务:
#conn.commit()
#cursor.close()
# 运行查询:
    count_i = 1
    count_x = 1
    __id = 0
    while True:
        cursor = conn.cursor()
        #cursor.execute(sql_select_one_str,[(count_x-1)*100,count_x*100])
        cursor.execute(sql_select_one_str1,[__id])
        #cursor.execute(sql_select_one_str1)
        values = cursor.fetchall()
        if len(values) == 0:
            conn.commit()
            break
        for vs in values:
            id_str = vs[0]
            __id = id_str
            content_str = vs[1]
            email_time = ac(content_str)
            print("id:%s" % id_str)
            print(email_time)
            if not email_time == None and not email_time == "":
                add_time_str = vs[2]
                #print("id:%s" % id_str)

                timedelta = add_time_str.replace(tzinfo=None) - datetime.strptime(email_time, '%Y-%m-%d %H:%M:%S').replace(tzinfo=None)
                #days[, #seconds[, microseconds[, milliseconds[, minutes[, hours[, weeks
                time_delta_int = (timedelta.days*24*60*60+timedelta.seconds)
                __cursor = conn.cursor()
                __cursor.execute(sql_update_str,[email_time,time_delta_int,id_str])
                __cursor.close()
            print(count_i)
            count_i = count_i + 1
        cursor.close()
        conn.commit()
        count_x = count_x + 1
    conn.close()


#导入MySQL驱动:
import mysql.connector
import time

while True:
    update_time_delta()
    time.sleep(120)

