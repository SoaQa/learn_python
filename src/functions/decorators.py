def decorator_one(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(args)
        print(kwargs)
        return result

    return wrapper
