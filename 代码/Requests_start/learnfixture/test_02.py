'''

fixture的作用域：
'''
import pytest
@pytest.fixture(scope="class")
def login():
    print("登陆系统")
    yield
    print("退出登陆")
class TestLogin:
    def test_case01(self):
        print("测试用例1")
    def test_case02(self,login):
        print("测试用例2")
    def test_case03(self,login):
        print("测试用例3")
    def test_case04(self,login):
        print("测试用例4")


    