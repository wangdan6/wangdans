'''
获取cookie:服务的响应中如果带了set-cookie ,可以通过r.cookies获取
'''
import requests
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
r=requests.get("http://www.baidu.com",headers=headers)
c=r.cookies
print(type(c)) #

cookies_dict=requests.utils.dict_from_cookiejar(c)
#遍历字典
for key,value in cookies_dict.items():
    print(key,value)



r=requests.get("https://www.baidu.com/s",params={"wd":"png是什么格式"},headers=headers,cookies=cookies_dict,verify=False)

assert("png" in r.text) 