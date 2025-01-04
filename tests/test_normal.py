import pytest

def test_1():
    print('1')

def test_2():
    print('2')


@pytest.mark.regression
def test_3():
    print('3')

@pytest.mark.xfail(reason='there is dependency')
def test_4():
    print('4')


@pytest.mark.skip(reason='there is dependency')
def test_5():
    print('5')

