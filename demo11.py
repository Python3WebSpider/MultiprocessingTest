from multiprocessing import Pool
import time


def function(index):
    print(f'Start process: {index}')
    time.sleep(3)
    print(f'End process {index}', )


if __name__ == '__main__':
    pool = Pool(processes=3)
    for i in range(4):
        pool.apply_async(function, args=[i])

    print('Main Process started')
    pool.close()
    pool.join()
    print('Main Process ended')
