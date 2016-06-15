from email.utils import parseaddr
from email.header import decode_header
from datetime import datetime,timedelta
import re

import yaml
import logging
import codecs
import json
import os
import sys
import base64
from models import email_part_entity
from models import email_entity
from util_mp import convert_to_builtin_type

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)

##Content-Transfer-Encoding
#quoted-printable
#base64
#7bit

##Content-Type
#multipart/alternative
#text/plain
#text/html

##charset
#UTF-8

from models import alert_entity
_logger = logging.getLogger(__name__)

def datacheck(ae):
    if ae.event_code != '':
        return True

#邮件内容装箱
def dismantle(em):
    ae = alert_entity.alert()
    _logger.debug("开始拆解邮件")
    lines = re.split("\r\n|\r|\n",em.content)
    lines = list(filter(lambda s: s and s.strip(), lines))
    print(lines)
    for l in lines:
        slice_str = l.strip().split(":",1)
        k = slice_str[0].lower()
        v = "".join(slice_str[1:]).strip()
        if v == "{}":
            v = ''
        if k == 'event_time':
            format_str = "%Y*%m*%d %H:%M:%S"
            if ':' not in v:
                format_str = format_str.replace(":","")
            if '-' in v:
                format_str = format_str.replace("*","-")
            elif '.' in v:
                format_str = format_str.replace("*",".")
            elif '/' in v:
                format_str = format_str.replace("*","/")
            ae.event_time = datetime.strptime(v,format_str).strftime("%Y-%m-%d %H:%M:%S")
        elif k == 'event_code':
            ae.event_code = v
        elif k == 'alert_code':
            ae.alert_code = v
        elif k == 'node':
            ae.node = v
        elif k == 'status':
            ae.status = v
        elif k == 'level':
            ae.level = v
        elif k  == 'title':
            ae.title = v
        elif k == 'hostrole':
            ae.hostrole = v
        elif k == 'host':
            ae.host = v
        elif k == 'hostgroup':
            _logger.debug("hostgroup value%s:" % v)
            ae.hostgroup = v
        elif k == 'data':
            ae.data = v.split("*UNKNOWN")[0]
    #return json.dumps(ae,default=convert_to_builtin_type)
    if datacheck(ae):
        return ae
    else:
        return None

def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset

def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value

def decode_base64(data):
    missing_padding = 4 - len(data) % 4
    if missing_padding:
        data += b'='* missing_padding
    return base64.decodestring(data)

#只有第一层解析From To Subject
def parse_x(content):
    #'Content-Transfer-Encoding' 7bit base64
    em = email_entity.email_enty()
    em.content = content
    ae = dismantle(em)
    if ae:
        return ae.event_time
    else:
        return None


#只有第一层解析From To Subject
def parse(msg,em,indent=0):
    #'Content-Transfer-Encoding' 7bit base64
    transfer_encoding = '7bit'
    if indent == 0:
        for header in ['From', 'To', 'Subject','Date','Content-Transfer-Encoding']:
            value = msg.get(header, '')
            if value:
                if header=='Subject':
                    value = decode_str(value)
                    em.subject = value
                elif header=='Date':
                    value = value.replace("(CST)","")
                    email_time_dt = datetime.strptime(value.strip(), '%a, %d %b %Y %H:%M:%S %z')
                    em.email_time = email_time_dt.strftime("%Y-%m-%d %H:%M:%S")
                elif header == 'Content-Transfer-Encoding':
                    transfer_encoding = decode_str(value).strip()
                    em.cte = transfer_encoding
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
    if (msg.is_multipart()):
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            em = parse(part, em, indent + 1)
    else:
        print("----------------999-----------------")

        __epe = email_part_entity.email_part_enty()
        content_type = msg.get_content_type()
        __epe.ct = content_type
        charset = guess_charset(msg)
        __epe.charset = charset
        print(__epe.ct)
        print(__epe.charset)
        if content_type=='text/plain' or content_type=='text/html':
            content = msg.get_payload()
            #print(charset)
            #if charset:
            #    content = content.decode(charset)
            print("--------------------")
            print(content)
            if transfer_encoding.lower() == 'base64':
                try:
                    content = decode_base64(bytes(content,encoding="utf-8"))
                except Exception as e:
                    try:
                        content = decode_base64(bytes(content,encoding="gb2312"))
                    except Exception as e:
                        pass
                content = bytes.decode(content)
            elif transfer_encoding.lower() == '7bit':
                try:
                    content = bytes(content,encoding="utf-8")
                except Exception as e:
                    try:
                        content = bytes(content,encoding="gb2312")
                    except Exception as e:
                        pass
                content = bytes.decode(content)
            __epe.cte = transfer_encoding.lower()
            __epe.content = content
        elif content_type=='application/octet-stream':
            content = msg.get_payload()
            
            if transfer_encoding.lower() == 'base64':
                try:
                    content = decode_base64(bytes(content,encoding="utf-8"))
                except Exception as e:
                    try:
                        content = decode_base64(bytes(content,encoding="gb2312"))
                    except Exception as e:
                        return None
                content = bytes.decode(content)
            __epe.cte = transfer_encoding.lower()
            __epe.content = content       
        else:
            print("**4**".center(80,"-"))
            print('%sAttachment: %s' % ('  ' * indent, content_type))
        em.contents.append(__epe)
        return em

if __name__ == '__main__':
    _logger.info("value")
    ae = alert_entity.alert()
    with codecs.open(os.path.abspath(".")+"/test_ae_obj",'r','utf-8') as f:
        a = dismantle(str(f.read()),ae)
        print(a)

