def func1():
    return True


def func2():
    return 4


def func3():
    return True


def func4():
    return {"key_1": True, "key_2": False, "key_4": 1, "key_5": 3}


def func5():
    return []


if __name__ == "__main__":
    assert func1() is True
    assert isinstance(func2(), int)
    assert func3() is True
    assert isinstance(func4(), dict) and func4()
    assert isinstance(func5(), list) and not func5()
    print("УРЯЯЯЯ!!!!")

