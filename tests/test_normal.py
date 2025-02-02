import pytest

def test_1():
    print('1')

def test_2():
    print('2')


@pytest.mark.regression
<<<<<<< HEAD
def test_3():
    print('3')

@pytest.mark.xfail(reason='there is dependency')
def test_4():
=======
def text_3():
    print('3')

@pytest.mark.xfail(reason='there is dependency')
def text_4():
>>>>>>> 6fb9acbb7c5c24ffcfdceefa990530a185da9bf4
    print('4')


@pytest.mark.skip(reason='there is dependency')
<<<<<<< HEAD
def test_5():
=======
def text_5():
>>>>>>> 6fb9acbb7c5c24ffcfdceefa990530a185da9bf4
    print('5')

