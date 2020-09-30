#pytest fixture 
#list 
import pytest
import sys
sys.path.append(r"F:\ZMN-王丹\apitest\代码\Requests_start")
from  jinrongzonghe.caw.DataRead import DataRead
from  jinrongzonghe.baw.Member import Member
from  jinrongzonghe.baw.DbOp import DbOp
from jinrongzonghe.caw.Ass import Assert

@pytest.fixture(params=DataRead().read_yaml(r"data_case\register_fail.yaml"))
def fail_data(request):
    return request.param

@pytest.fixture(params=DataRead().read_yaml(r"data_case\register_success.yaml"))
def success_data(request):
    return request.param

@pytest.fixture(params=DataRead().read_yaml(r"data_case\register_repeat.yaml"))
def repeat_data(request):
    return request.param

# print(fail_data)

# print(success_data)


def test_register_fail(fail_data,url,base_requests):
    print(f"执行注册失败的用例，测试数据为{fail_data}")
    r=Member().register(url,base_requests,fail_data['data'])
    print(r.json())
    assert fail_data["except"]["msg"]==r.json()["msg"]
    Assert().equal(fail_data["except"],r.json(),"code,status,msg")



def test_register_success(success_data,url,base_requests,db):
    DbOp().delete_user(db,success_data["data"]["mobilephone"])
    re=Member().register(url,base_requests,success_data["data"])
    print(re.text)
    assert success_data["expect"]["msg"]==re.json()["msg"]
    #"清理环境"
    DbOp().delete_user(db,success_data["data"]["mobilephone"])
def test_register_repeat(repeat_data,url,base_requests,db):
    re=Member().register(url,base_requests,repeat_data["data"])
    assert repeat_data["expect"]["msg"]==re.json()["msg"]

