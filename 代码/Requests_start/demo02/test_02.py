'''
'''
def setup_module():
    print("测试前置，整个模块开始前执行")
def teardown_module():
    print("测试后置，整个模块结束")
def setup_function():
    print("测试前置.每个方法开始前执行")
def teardown_function():
    print("测试后置，每个方法结束后执行")
def test_case01():
    print("测试用例1")

def test_case02():
    print("测试用例2")