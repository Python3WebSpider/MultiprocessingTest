import multiprocessing
import time


def process(index):
    time.sleep(index)
    print(f'Process: {index}')


if __name__ == '__main__':
    for i in range(5):
        p = multiprocessing.Process(target=process, args=(i,))
        p.start()

    print(f'CPU number: {multiprocessing.cpu_count()}')
    for p in multiprocessing.active_children():
        print(f'Child process name: {p.name} id: {p.pid}')
    print('Process Ended')
