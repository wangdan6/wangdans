# import pytest
def a(f):
    def b():
        print("4")
        f()
        print(5)
def test_case01():
    print("3")
a(test_case01)


