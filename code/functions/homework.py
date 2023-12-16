import sys


if __name__ == "__main__":
    this_mod = sys.modules[__name__]

    square_of_int = getattr(this_mod, 'kilometers_to_centimeters')
    for i in range(10):
        assert square_of_int(i) == i * 1000

    strip_rows = getattr(this_mod, "strip_rows")

    stripped_rows = strip_rows(rows=[" Hi", "Python ", " It "])

    for i in stripped_rows:
        assert " " not in i
