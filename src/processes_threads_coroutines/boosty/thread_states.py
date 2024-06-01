import threading
import time


class MyThread(threading.Thread):
    def __init__(self, name, sleep=5):
        threading.Thread.__init__(self)
        self.name = name
        self.sleep = sleep

    def run(self):
        print("Starting " + self.name)
        time.sleep(self.sleep)


if __name__ == '__main__':
    thread = MyThread(name='МойПоток')
    daemon_thread = MyThread(name="Daemon", sleep=500)
    daemon_thread.daemon = True

    print(thread.is_alive())

    thread.start()
    daemon_thread.start()

    print(thread.is_alive())

    print(threading.active_count())
    print(threading.enumerate())
