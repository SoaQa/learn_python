
class MyIterator:
    def __init__(self, my_coll):
        self._my_coll = my_coll
        self.last_returned = None

    def __next__(self):
        if self.last_returned is None:
            self.last_returned = "a"
            return self._my_coll.a

        elif self.last_returned == "a":
            self.last_returned = "b"
            return self._my_coll.b

        elif self.last_returned == "b":
            self.last_returned = "c"
            return self._my_coll.c

        else:
            raise StopIteration()


class MyCollection:
    def __init__(self, a=None, b=None, c=None):
        self.a = a
        self.b = b
        self.c = c

    def __iter__(self):
        return MyIterator(self)


my_collection = MyCollection(a=1, b="a", c={"a": 22})

for i in my_collection:
    print(i)
