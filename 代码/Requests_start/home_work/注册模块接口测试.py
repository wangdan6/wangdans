import requests
#代理抓包定位问题，查看参数默认参数
proxy={
    "http":"http://127.0.0.1:8888",
    "https":"http://127.0.0.1:8888"
}
# requests.get("http://127.0.0.1:8080/futureloan/mvc/api/member/register",proxies=proxy)
#1.用例1，正常，reg
url="http://192.168.150.222/futureloan/mvc/api/member/loginreg"
account={"mobilephone":"18089269982","pwd":"123456"}
r=requests.post(url,data=account)
print(r.text)


# #2.用例2，为空异常1.1：手机号为空
# url="http://192.168.150.222:8081/futureloan/mvc/api/member/login"
# account={"mobilephone":"","pwd":"123456"}
# r=requests.post(url,data=account)
# print(r.text)

# #3.用例3.为空异常1.2:密码为空
# url="http://192.168.150.222:8081/futureloan/mvc/api/member/login"
# account={"mobilephone":"18089269982","pwd":""}
# r=requests.post(url,data=account)
assert r.status_code=="20103"

# print(r.text)
# #4.用例4.用户名（手机号）或密码错误异常1.1：手机号错误
# url="http://192.168.150.222:8081/futureloan/mvc/api/member/login"
# account={"mobilephone":"18089269982","pwd":"123456"}
# r=requests.post(url,data=account)
# print(r.text)
# #5.用例5.用户名（手机号）或密码错误异常1.2：密码错误
# url="http://192.168.150.222:8081/futureloan/mvc/api/member/login"
# account={"mobilephone":"18089269982","pwd":"1234567"}
# r=requests.post(url,data=account)
# print(r.text)