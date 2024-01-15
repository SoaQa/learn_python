class MyIterator:
    def __init__(self, c):
        self.last_returned = None
        self.c = c

    def __next__(self):
        if self.last_returned is None:
            self.last_returned = "a"
            return self.c.a

        elif self.last_returned == "a":
            self.last_returned = "b"
            return self.c.b

        elif self.last_returned == "b":
            self.last_returned = "c"
            return self.c.c

        else:
            raise StopIteration()


class MyCollection:
    def __init__(self, a=None, b=None, c=None):
        self.a = a
        self.b = b
        self.c = c
        self.last_returned = None

    def __iter__(self):
        return MyIterator(self)


my_collection = MyCollection(a=1, b="a", c={"a": 1})

for i in my_collection:
    print(i)

# for i in {"my_collection": 1, "my_collection2": 2, "my_collection3": 3}:
#     print(i)
