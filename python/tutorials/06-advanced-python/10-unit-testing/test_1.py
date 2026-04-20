def add(a,b):
    return a+b

def test_add():
    assert add(2,3) == 5
    assert add(10,-5) == 5
    assert add(-1,-3) == -4

def test_add_neg():
    assert add(-10,-11) == -21
    assert add(-100,-110) == -210

def test_add_big():
    assert add(1000000, 2000000) == 3000000
    assert add(2000000000, 5000000000) == 7000000000
