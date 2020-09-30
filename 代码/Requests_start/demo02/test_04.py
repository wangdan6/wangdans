'''
mark标记实现参数化
'''
import pytest
import requests
url="http://192.168.150.52:8089/futureloan/mvc/api/member/register"

case_data=[("18089269999","123456","投资人","手机号码已被注册","20110",0),
("180","888","借款人","密码长度必须为6~18","20108",0)]
@pytest.mark.parametrize("mobile,pwd,regname,msg,code,status",case_data)
def test_register(mobile,pwd,regname,msg,code,status):
    param={"mobilephone":mobile,"pwd":pwd,"regname":regname}
    r=requests.post(url,data=param)
    print(r.status_code)
    assert r.json()["msg"]==msg
    assert r.json()["code"]==code
    assert r.json()["status"]==status
withdraw_data=[("18089269999","10")]
# @pytest.mark.skip("该接口为实现，本版本暂不执行")
@pytest.mark.skipif(1==2,reason="前面表达式为true时，跳过；表达式为false时，不跳过")
@pytest.mark.parametrize("mobile,amount",withdraw_data)
def test_withdraw(mobile,amount):
    url="http://192.168.150.52:8089/futureloan/mvc/api/member/withdraw"
    param={"mobilephone":mobile,"amount":amount}
    ret=requests.post(url,data=param)
    assert ret.json()["msg"]!="服务器异常"