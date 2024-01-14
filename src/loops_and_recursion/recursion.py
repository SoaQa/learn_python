my_dict = {
    'a': 1,
    'b': 2,
    'c': {
        'a': {
            'a': 1,
            'b': 2,
            'c': {
                'b': {
                    'a': 1,
                    'b': 2,
                    'c': {
                        'a': 10
                    }
                }
            }
        },
        'b': "Hello"
    }
}


def recursion(value: dict):
    for k, v in value.items():
        if isinstance(v, dict):
            recursion(v)
        else:
            print(f'{k} = {v}')


recursion(my_dict)
