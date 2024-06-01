import os


def child_process():
    """Функция для дочернего процесса."""
    print(f'Привет от дочернего процесса! PID: {os.getpid()}, родительский PID: {os.getppid()}')


def parent_process(child_pid):
    """Функция для родительского процесса."""
    print(f'Привет от родительского процесса! PID: {os.getpid()}, дочерний PID: {child_pid}')


if __name__ == '__main__':
    pid = os.fork()

    if pid == 0:
        # Мы в дочернем процессе
        child_process()
    else:
        # Мы в родительском процессе
        parent_process(pid)
