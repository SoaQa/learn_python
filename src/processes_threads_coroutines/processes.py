import random
from time import sleep
import multiprocessing
import os


def main():
    for i in range(10):
        print(os.getpid())
        sleep(random.randint(1, 5))


if __name__ == '__main__':
    proc = multiprocessing.Process(target=main)
    proc.start()
    main()
