import multiprocessing
import time

result_list2 = []


def main(from_int, to_int, rl):
    global result_list2
    result = 0
    for i in range(from_int, to_int):
        result += i ** 2

    rl.append(result)
    result_list2.append(result)


if __name__ == '__main__':
    start = time.time()
    manager = multiprocessing.Manager()
    result_list = manager.list()

    proc1 = multiprocessing.Process(target=main, args=(1, 5_000_000, result_list))
    proc2 = multiprocessing.Process(target=main, args=(5_000_000, 10_000_000, result_list))

    proc1.start()
    proc2.start()

    proc1.join()
    proc2.join()

    print(sum(result_list))
    print(sum(result_list2))
    print(time.time() - start)
