import pytest
import sys
sys.path.append(r"F:\ZMN-王丹\apitest\代码\Requests_start")
from jinrongzonghe.caw.DataRead import DataRead
from jinrongzonghe.caw.BaseRequests import BaseRequests
from  jinrongzonghe.baw.DbOp import DbOp
from jinrongzonghe.baw.Member import Member
ENVPATH=r"data_env\env.ini"

@pytest.fixture(scope="session")
def url():
    return DataRead().read_ini(ENVPATH,'url')

@pytest.fixture(scope="session")
def db():
    return eval(DataRead().read_ini(ENVPATH,'db'))

#BaseRequests 
@pytest.fixture(scope="session")
def base_requests():
    return BaseRequests()

# @pytest.fixture(params=DataRead().read_yaml(r"data_case\login_setup.yaml"))
# def login_setup_data(request):
#     return request.param
# @pytest.fixture()
# def register(login_setup_data,url,base_requests,db):
#     Member().register(url,base_requests,login_setup_data["data"])
#     yield
#     #删除注册用户
#     DbOp().delete_user(db,login_setup_data["data"]["mobilephone"])
    