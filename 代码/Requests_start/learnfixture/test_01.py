'''
'''
import pytest

@pytest.fixture(autouse=True)
def data():
    print("准备测试数据")



@pytest.fixture()
def login():
    print("登陆功能")
    yield
    print("yield之后是后置")
@pytest.mark.usefixtures("login")
def test_register():
    print("注册功能，不用登陆")
def test_recharge(login):
    print("充值功能，需要先登录")


def test_withdraw(login):
    print("取现功能，需要先登录")