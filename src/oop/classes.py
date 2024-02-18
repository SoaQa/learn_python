from abc import abstractmethod, ABC

import requests


class AbstractTextReader(ABC):
    @abstractmethod
    def read_text(self):
        ...


class RESTApiTextReader(AbstractTextReader):
    def __init__(self, url):
        self.url = url

    def read_text(self):
        response = requests.get(self.get_url())
        print(response.text)

    def get_url(self):
        return self.url


class TextReader(AbstractTextReader):
    def __init__(self, file_name):
        self.file_name = file_name

    def read_text(self, ):
        with open(self.file_name) as f:
            print(f.read())


# readers = {
#     "text": TextReader("text"),
#     "text2": TextReader("text2"),
# }
#
# readers["text"].read_text()
# readers["text2"].read_text()


class ClassTextReader(AbstractTextReader):
    file_name = "text2"

    @classmethod
    def read_text(cls, ):
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


if __name__ == "__main__":
    readers = [
        RESTApiTextReader("http://ip.jsontest.com/"),
        TextReader("text"),
        ClassTextReader(),
    ]

    for i in readers:
        i.read_text()
