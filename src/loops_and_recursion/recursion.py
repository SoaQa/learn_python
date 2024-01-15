my_dict = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': {
        "a": 4,
        "b": {
            "a": 5,
            "b": {
                "a": 6
            }
        }
    }
}


def dict_traversal(d: dict):
    for v in d.values():
        if isinstance(v, dict):
            dict_traversal(v)
        else:
            print(v)


dict_traversal(my_dict)
