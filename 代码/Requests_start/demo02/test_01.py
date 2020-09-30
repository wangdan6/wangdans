'''
'''
import pytest
def add(a,b):
    try:
        return a+b
    except  Exception as e:
        return str(e).strip()

def test_case01():
    ret=add(1,2)
    assert ret==3
def test_case02():
    ret =add(0.1,0.2)
    assert ret ==0.3
def test_case03():
    ret=add([1,2],[3,4])
    assert ret==[1,2,3,4]
def test_case04():
    ret =add(1,"1")
    assert ret ==""

