'''
装饰器：运行中增加功能的一种方式
'''

def log(func):
    def wrapper(func,*args,**kw):
        print(f"in 函数{func.__name__}")
        func(*args,**kw)
        print(f"out 函数{func.__name__}")
        return wrapper
def test_case1():
    print("in 函数：test_case1")
    print("用例1")
    print("out 函数：test_case01")
@log
def test_case2():
    print("用例2")
