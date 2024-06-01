import asyncio
import time

result_list2 = []


async def calc(from_int, to_int):
    global result_list2
    result = 0
    for i in range(from_int, to_int):
        result += i ** 2

    result_list2.append(result)


async def main():
    start = time.time()

    await asyncio.gather(calc(1, 5_000_000), calc(5_000_000, 10_000_000))

    print(sum(result_list2))
    print(time.time() - start)


if __name__ == '__main__':
    asyncio.run(main())
