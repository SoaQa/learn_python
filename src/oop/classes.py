class TextReader(object):
    def __init__(self, file_name):
        self.file_name = file_name

    def read_text(self,):
        with open(self.file_name) as f:
            print(f.read())


# readers = {
#     "text": TextReader("text"),
#     "text2": TextReader("text2"),
# }
#
# readers["text"].read_text()
# readers["text2"].read_text()


class ClassTextReader(object):
    file_name = "text2"

    @classmethod
    def read_text(cls,):
        with open(cls.file_name) as f:
            print(f.read())

#
# readers = {
#     "text": ClassTextReader(),
#     "text2": ClassTextReader(),
# }
#
# readers["text"].read_text()
# readers["text2"].read_text()
#
# ClassTextReader.file_name = "text1"
#
# readers["text"].read_text()
# readers["text2"].read_text()
