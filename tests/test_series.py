from math_series.series import fibonacci, lucas, sum_series


def test_fib_1():
    assert fibonacci(2) == 1


def test_fib_2():
    assert fibonacci(10) == 55


def test_fib_3():
    assert fibonacci(5) == 5


def test_fib_4():
    assert fibonacci(4) == 3


def test_fib_5():
    assert fibonacci(19) == 4181


def test_lucas_1():
    assert lucas(1) == 1


def test_lucas_2():
    assert lucas(6) == 18


def test_lucas_3():
    assert lucas(8) == 47


def test_lucas_4():
    assert lucas(10) == 123


def test_lucas_5():
    assert lucas(5) == 11

def test_sum_series_as_default(): #fibonacci 
    assert sum_series(18) == 2584

def test_sum_series_as_random_series():
    assert sum_series(7 ,default1 = 3 ,default2 = 5) == 89

def test_sum_series_as_random_series():
    assert sum_series(5 ,default1 = 1 ,default2 = 5) == 28

def test_sum_series_as_lucas():
    assert sum_series(10 ,2 ,1) == 123