'''

fixture的作用域：
'''
import pytest
@pytest.fixture(scope="module")
def login():
    print("登陆系统")
    yield
    print("退出登陆")

@pytest.fixture(scope="module")
def dabase():
    print("链接数据库")
    yield
    print("断开数据库")
class TestLogin:
    def test_case01(self):
        print("测试用例1")

    def test_case02(self,login):
        print("测试用例2")
    
    def test_case03(self,login):
        print("测试用例3")
    def test_case04(self,login):
        print("测试用例4")
class TestLogin02:
    def test_case01(self,dabase):
        print("测试用例001")

    def test_case02(self,login):
        print("测试用例002")
    