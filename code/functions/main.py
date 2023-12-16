foo = "Hello"


def square_of_int(digit: int, r: str = None, s: int = 2) -> int:
    result = digit ** s

    if r:
        print(r)
    print(foo)
    return result


print(square_of_int(6))


def bar():
    ...

s = bar()
if s is None:
    print("s is None")
print(s)


def outer():
    b = "Hello"

    def inner():
        print(b)
        print(foo)

        for i in s_l:
            print(i)

    s_l = ["a", "b", "C"]
    inner()


outer()


def bar(*args: int, **kwargs):
    for i in args:
        print(i)

    for k, v in kwargs.items():
        print(k, " ", v)


bar(1, 2, 3,)
bar(a=1, b=2, c=3)
bar(5, 6, 7, a=1, b=2, c=3)


my_tuple = (1, 2, 3,)
my_list = [1, 2, 3,]

my_list.append(4)
print(my_list)

print(id(my_list))
print(id(my_tuple))


def foobar(mlist:list, mtuple: tuple):
    print(id(mlist))
    print(id(mtuple))

    mlist.append(5)


foobar(my_list, my_tuple)
print(my_list)
