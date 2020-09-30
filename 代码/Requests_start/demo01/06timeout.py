#测试接口性能
import requests
for i in range(10):
    try:
        canshu={"tel":"18089269982"}
        r=requests.get("https://tcc.taobao.com/cc/json/mobile_tel_segment.htm",params=canshu,timeout=i/100.0)
        print(r.status_code)#request.exception.connecttimeout
    except Exception as e:
        print(e)


