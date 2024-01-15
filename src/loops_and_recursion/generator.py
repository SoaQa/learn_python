def file_lines_generator(filename):
    with open(filename, "r") as file:
        while line := file.readline():
            yield line


for lines in file_lines_generator("sample"):
    print(lines)
