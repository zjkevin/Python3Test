s = "\u7ea2\u5c71\u673a\u623f-\u6570\u636e\u5e93-MYSQL, \u8fd0\u8425\u652f\u6491\u90e8-\u57fa\u7840-\u76d1\u63a7\u5e73\u53f0"
ss = s.encode('utf-8','ignore')
ss.decode()
print(s)
print(ss)
print(ss.decode())


# bytes object  
b = b"example"  

# str object  
s = "example"  

# str to bytes  
bytes(s, encoding = "utf8")  

# bytes to str  
str(b, encoding = "utf-8")  

# an alternative method  
# str to bytes  
str.encode(s)  

# bytes to str  
bytes.decode(b)  
