class TextReader(object):
    file_name = "text"

    def __init__(self, file_name):
        self.file_name = file_name

    @classmethod
    def read_text(cls, file_name):
        print(cls(file_name))
