import faker
import pytest
f=faker.Faker()

@pytest.fixture()
def username():
    return f.user_name()

@pytest.fixture()
def pwd():
    return f.password()

@pytest.fixture()
def get_user_pwd(username,pwd):
    return {'username':username,'pwd':pwd}

def test_login(get_user_pwd):
    print(f"测试登陆功能，登陆的用户名：{get_user_pwd['username']}密码为:{get_user_pwd['pwd']}")



