import pytest
class TestClass01:
    def setup_class(self):
        print("测试前置，类里所有用例开始前执行")
    def teardown_class(self):
        print("测试后置，类内所有用例结束时执行")
    # def setup(self):
    def setup_method(self):
        print("每个方法前执行")
    # def teardown_method(self):
    def teardown(self):
        print("每个方法后执行")
    def test_case01(self):
        print("1")
    def test_case02(self):
        print("2")
if __name__ == "__main__":
    pytest.main([r"F:\ZMN-王丹\apitest\代码\Requests_start\demo02\test_03.py"])