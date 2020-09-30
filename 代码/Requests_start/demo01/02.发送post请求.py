'''
发送post请求
1.使用data传参
2.使用json传参
'''
import requests

#1.data传参
# url="http://httpbin.org/post"
# canshu={"username":"root","password":"123456"}
# r=requests.post(url,data=canshu)#使用data传参“content_Type=application/x-www-form-urlencoded”
# print(r.text)
#
# #2.json传参
# r=requests.post(url,json=canshu)#使用json传参“content_Type=application/json”
# print(r.text)


#金融项目，登陆接口，post
url="http://192.168.150.52:8089/futureloan/mvc/api/member/login"
account={"mobilephone":"18089269982","pwd":"123456","regname":"auto"}
r=requests.post(url,data=account)
print(r.text)

r=requests.post(url,json=account)
print(r.text)




