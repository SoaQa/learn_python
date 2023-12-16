def square_of_int(digit: int, r: str = None, s: int = 2) -> int:
    result = digit ** s

    if r:
        print(r)

    return result


def bar():
    ...

s = bar()
if s is None:
    print("s is None")
print(s)
