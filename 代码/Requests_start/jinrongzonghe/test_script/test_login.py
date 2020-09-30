import pytest
import sys
sys.path.append(r"F:\ZMN-王丹\apitest\代码\Requests_start")
from  jinrongzonghe.caw.DataRead import DataRead
from  jinrongzonghe.baw.Member import Member
from  jinrongzonghe.baw.DbOp import DbOp
from jinrongzonghe.caw.Ass import Assert

# @pytest.fixture(params=DataRead().read_yaml(r"data_case\login_fail.yaml"))
# def lofail_data(request):
#     return request.param
@pytest.fixture(params=DataRead().read_yaml(r"data_case\login_success.yaml"))
def login_data(request):
    return request.param

@pytest.fixture(params=DataRead().read_yaml(r"data_case\login_setup.yaml"))
def login_setup_data(request):
    return request.param





# def test_login_fail():
#     pass
# def test_login_success(losuccess_data,url,base_requests,db):
#     re=Member().login(url,base_requests,losuccess_data["data"])
#     print(re.json())
#     print(losuccess_data["expect"])
#     Assert().equal(losuccess_data["expect"],re.json(),"status,msg")

@pytest.fixture()
def register(login_setup_data,url,base_requests,db):
    Member().register(url,base_requests,login_setup_data["data"])
    yield
    #删除注册用户
    DbOp().delete_user(db,login_setup_data["data"]["mobilephone"])
def test_login(register,url,base_requests,db,login_data):
    #登陆的测试逻辑
    re=Member().login(url,base_requests,login_data["data"])
    print(re.json())
    print(login_data["expect"])
    Assert().equal(login_data["expect"],re.json(),"status,msg")