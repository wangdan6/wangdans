import pytest
import requests
#测试数据，可以从csv读取，也可以从xml读取，也可以从yaml文件中读取
data=[{"data":{"mobilephone":"18012345678","pwd":"123456"},"expect":{'status': 0, 'code': '20110', 'data': None, 'msg': '手机号码已被注册'}},
      {"data":{"mobilephone":"18012345679","pwd":"1234"},"expect":{'status': 0, 'code': '20108', 'data': None, 'msg': '密码长度必须为6~18'}}]

@pytest.fixture(params=data)
def register_datar(request):
    return request.param

def test_register(register_datar):
    print(register_datar)
    ret=requests.post("http://192.168.150.52:8089/futureloan/mvc/api/member/register",register_datar["data"])
    print(ret.json())
    assert ret.json()==register_datar["expect"]
def test_list():
    ret=re
    
