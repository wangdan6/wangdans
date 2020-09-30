#三个参数时：传参数：正交
import pytest
@pytest.fixture(params=["大写","小写","混合"])
def data_string(request):
    return request.param

@pytest.fixture(params=['向上','向下'])
def data_fangxiang(request):
    return request.param

@pytest.fixture(params=["是","否"])
def data_qufen(request):
    return request.param

#如果有多个参数，多个参数全排列
def test_search(data_string,data_fangxiang,data_qufen):
    print(f"要搜索的字符串为{data_string}搜索方向为{data_fangxiang}是否区分大小写为{data_qufen}")
