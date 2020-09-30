'''
业务AW:按模块划分
business action word
'''
REGISTER="futureloan/mvc/api/member/register"
LOGIN="futureloan/mvc/api/member/login"
class Member:
    def register(self,url,base_requests,data):
        '''
        '''
        real_url=url+REGISTER
        r=base_requests.post(real_url,data=data)
        return r
        
    def login(self,url,base_requests,data):
        real_url=url+LOGIN
        r=base_requests.post(real_url,data=data)
        return r
if __name__ == "__main__":
    import sys
    sys.path.append(r"F:\ZMN-王丹\apitest\代码\Requests_start")
    from jinrongzonghe.caw.BaseRequests import BaseRequests
    r=Member().register("http://192.168.150.222:8081/",BaseRequests(),{"mobilephone":"145345"})
    print(r.text)