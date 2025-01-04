import pytest

def test_1():
    print('1')

def test_2():
    print('2')


@pytest.mark.regression
def text_3():
    print('3')

@pytest.mark.xfail(reason='there is dependency')
def text_4():
    print('4')


@pytest.mark.skip(reason='there is dependency')
def text_5():
    print('5')

