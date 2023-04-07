from NWD_user import nwd

def test_ndw_1_1():
    assert nwd(1, 1) == 1

def test_ndw_1_3():
    assert nwd(1, 3) == 1

def test_ndw_3_1():
    assert nwd(3, 1) == 1

def test_ndw_15_10():
    assert nwd(15, 10) == 5

def test_ndw_10_15():
    assert nwd(10, 15) == 5

def test_ndw_20_30():
    assert nwd(20, 30) == 10

def test_ndw_30_20():
    assert nwd(30, 20) == 10

def test_ndw_1071_462():
    assert nwd(1071, 462) == 21

def test_ndw_462_1071():
    assert nwd(462, 1071) == 21
