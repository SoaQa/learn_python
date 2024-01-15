my_list: list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


for i in my_list:
    print(i**2)


with open("sample", "r") as file:
    for i in file.readlines():
        print(i)

print(file.readlines())
