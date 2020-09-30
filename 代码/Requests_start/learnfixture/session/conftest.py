'''
conftest.py:存放
'''
import pytest

@pytest.fixture(scope="session")
def login():
    print("登陆")
    yield
    print("退出登陆")
@pytest.fixture(scope="session")
def db():
    print('链接数据库')
    yield
    print("断开数据库")