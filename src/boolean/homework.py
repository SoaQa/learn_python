def func1():
    ...


def func2():
    ...


def func3():
    return 1 or 1 > 0 and 10 > 11 and 4 > 5 or 1 > 0 or 4 < 4


def func4():
    ...


def func5():
    ...


if __name__ == "__main__":
    assert func1() is True
    assert isinstance(func2(), int)
    assert func3() is True
    assert isinstance(func4(), dict) and func4()
    assert isinstance(func5(), list) and not func5()

