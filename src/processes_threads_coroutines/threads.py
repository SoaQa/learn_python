import threading
import datetime
from uuid import uuid4

import requests


img_urls = [
    "https://kittypryde.ru/wp-content/uploads/2019/12/kotyata-v-korzinke.jpg",
    "https://proprikol.ru/wp-content/uploads/2020/08/krasivye-kartinki-kotikov-52.jpg",
    "https://mykaleidoscope.ru/uploads/posts/2022-08/1660398901_49-mykaleidoscope-ru-p-oboi-s-kotikami-na-stenu-dizain-krasivo-fo-51.jpg",
    "https://kittypryde.ru/wp-content/uploads/2019/12/kotyata-v-korzinke.jpg",
    "https://proprikol.ru/wp-content/uploads/2020/08/krasivye-kartinki-kotikov-52.jpg",
    "https://mykaleidoscope.ru/uploads/posts/2022-08/1660398901_49-mykaleidoscope-ru-p-oboi-s-kotikami-na-stenu-dizain-krasivo-fo-51.jpg",
]


def main(urls):
    print(len(urls))
    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            with open(f"images/{uuid4().hex}.{url.split('.')[-1]}", 'wb') as f:
                f.write(response.content)
        else:
            print(url)


if __name__ == '__main__':
    start = datetime.datetime.now()

    thread1 = threading.Thread(target=main, args=(img_urls[:3], ))
    thread2 = threading.Thread(target=main, args=(img_urls[3:], ))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(datetime.datetime.now() - start)
