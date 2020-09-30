import pytest
@pytest.mark.smoke
def test_case01():
    print("test_case01")

@pytest.mark.func
def test_case02():
    print("test_case02")

@pytest.mark.func
class TestClass:
    @pytest.mark.smoke
    def test_case03(self):
        print("test_case03")
    def test_case04(self):
        print("test_case04")
    def test_case05(self):
        print("test_case05")