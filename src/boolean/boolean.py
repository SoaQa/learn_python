expression_result: bool = True
false_expression_result: bool = False

expression_result = 0 >= 1
print(expression_result)


def check_digit():
    digit = int(input("Input a digit: "))

    if digit > 10:
        print(f"{digit} > 10")
    elif digit == 10:
        print(f"{digit} == 10")
    elif digit == 11:
        print(f"{digit} == 11")
    else:
        print(f"{digit} < 10")


user_list: list = []
user_dict: dict = {}

if user_dict or user_list and 1 > 10 or 1 > 0:
    print("user_dict or user_list is not empty")
else:
    print("user_dict and user_list is empty")


a = "hello"

if a is True:
    print("a is True")
else:
    print(f"{a} - {bool(a)}")
