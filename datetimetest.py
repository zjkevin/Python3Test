from datetime import datetime,timedelta
import time
#print(datetime.strftime("17 May 2016 08:25:15"))
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(int(cday.timestamp()))
#print(datetime.strftime("Tue, 17 May 2016 08:25:15 +0800"))


def testfunc(v):
    format_str = "%Y*%m*%d %H:%M:%S"
    if ':' not in v:
        format_str = format_str.replace(":","")
    if '-' in v:
        format_str = format_str.replace("*","-")
    elif '.' in v:
        format_str = format_str.replace("*",".")
    elif '/' in v:
        format_str = format_str.replace("*","/")
    print(v)
    print(format_str)

testfunc("2016-12-20 13:13:13")
testfunc("2016-12-20 131313")
testfunc("2016-12-20 13:13:13")
testfunc("2016.12.20 13:13:13")
testfunc("2016/12/20 13:13:13")

dt = datetime.now()
print(dt)
print(time.strftime("%Y-%m-%d %X %b", time.localtime()))
dt = datetime.strptime('Thu, 26 May 2016 13:18:27 +0800', '%a, %d %b %Y %H:%M:%S %z')
print(dt.strftime("%Y-%m-%d %H:%M:%S %z"))
#testfunc("2016-12-20 13:13:13")

dt = datetime.now()
print(dt)
print((dt + timedelta(minutes=-30)))
#scan_start_dt + datetime.timedelta(minutes=-30)).timestamp()

j_s = r"\\udsdsd\\u7868"
j_s = j_s.replace(r'\\n',r'\n')
print(j_s)