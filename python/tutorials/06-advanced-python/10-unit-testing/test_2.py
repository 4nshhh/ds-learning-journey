import pytest


def multiply(a,b):
    return a*b

def divide(a,b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by Zero")
    return a/b

def test_multiply():
    assert multiply(3,4) == 12
    assert multiply(10,2) == 20
    
def test_divide():
    assert divide(10,2) == 5
    with pytest.raises(ZeroDivisionError):
        divide(10,0)

