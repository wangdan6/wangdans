'''
发送get请求：
'''
import requests #导入包

# url="http://www.baidu.com"
# r=requests.get(url) #发送get请求，使用变量r接收响应
# # print(r.text)#文本类型的
# # print(r.status_code) #状态码
# # print(r.reason) #状态原因 OK
# # print(r.cookies)#响应信息的cookies
# # print(r.headers)#响应的头部信息
# # print(r.raw)#原始格式的
# # print(r.raw.read(10))
#
# # #金融项目注册
# #方法1
# url="http://192.168.150.222:8081/futureloan/mvc/api/member/register?mobilephone=18089269982&pwd=123456&regname=auto"
# r=requests.get(url)
#
# print(r.text)
# #方法2：使用params传参
# url="http://192.168.150.52:8089/futureloan/mvc/api/member/register"
# canshu={"mobilephone":"18089269931","pwd":"123457","regname":"test"}
# r=requests.get(url,params=canshu)
# print(r.text)

#httpbin,一个测试网站，有get/post等接口，参数任意构造，服务器讲发送的请求转成json格式的返回

# r=requests.get("http://www.httpbin.org/get?username=123&pwd=456&email=123456@qq.com")
# print(r.text)


# canshu={"tel":"18089269982"}
# r=requests.get("https://tcc.taobao.com/cc/json/mobile_tel_segment.htm",params=canshu)
# print(r.text)

#发送带请求头的
#设置
# header={
    # "User-Agent": "Microsoft-CryptoAPI/6.1"
# }
# r=requests.get("http://www.httpbin.org/get?username=123&pwd=456&email=123456@qq.com",headers=header)
# print(r.text)

#既带参数，又带请求头
#requests.get(url,params=,headers=)




