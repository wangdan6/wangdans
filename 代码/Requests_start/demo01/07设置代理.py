#爬虫之类的场景，避免服务器认为是供给，讲IP屏蔽掉
#代理抓包，定位问题
import requests
proxy={
    "http":"http://127.0.0.1:8888",
    "https":"http://127.0.0.1:8888"
}
requests.get("https://tcc.taobao.com/cc/json/mobile_tel_segment.htm",proxies=proxy)
# requests.get('http://www.httpbin.org')