import asyncio
import datetime
from uuid import uuid4

import aiohttp


img_urls = [
    "https://kittypryde.ru/wp-content/uploads/2019/12/kotyata-v-korzinke.jpg",
    "https://proprikol.ru/wp-content/uploads/2020/08/krasivye-kartinki-kotikov-52.jpg",
    "https://mykaleidoscope.ru/uploads/posts/2022-08/1660398901_49-mykaleidoscope-ru-p-oboi-s-kotikami-na-stenu-dizain-krasivo-fo-51.jpg",
    "https://kittypryde.ru/wp-content/uploads/2019/12/kotyata-v-korzinke.jpg",
    "https://proprikol.ru/wp-content/uploads/2020/08/krasivye-kartinki-kotikov-52.jpg",
    "https://mykaleidoscope.ru/uploads/posts/2022-08/1660398901_49-mykaleidoscope-ru-p-oboi-s-kotikami-na-stenu-dizain-krasivo-fo-51.jpg",
]


async def img_loader(urls, session):
    print(len(urls))
    for url in urls:
        async with session.get(url) as response:
            if response.status == 200:
                with open(f"images/{uuid4().hex}.{url.split('.')[-1]}", 'wb') as f:
                    f.write(await response.read())
            else:
                print(url)


async def main():
    start = datetime.datetime.now()
    async with aiohttp.ClientSession() as session, asyncio.TaskGroup() as tg:
        tg.create_task(
            img_loader(img_urls[:3], session)
        )
        tg.create_task(
            img_loader(img_urls[3:], session)
        )
    print(datetime.datetime.now() - start)


if __name__ == '__main__':
    asyncio.run(main())
