import requests
s=requests.Session()

print(s.cookies)
r=s.get("https://www.bagevent.com")
s=s.cookies
print(s)
jar=requests.utils.dict_from_cookiejar(s.cookies)
print(jar)
param={
    "access_type":1,
    "loginType":1,
    "emailLoginWay":0,
    "account":"2780487875@qq.com",
    "password":"qq2780487875",
    "remindme":1
}
r=s.post("https://www.bagevent.com/user/login",data=param)
print(s)
print(jar)
