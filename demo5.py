from multiprocessing import Process
import time


class MyProcess(Process):
    def __init__(self, loop):
        Process.__init__(self)
        self.loop = loop

    def run(self):
        for count in range(self.loop):
            time.sleep(0.001)
            print(f'Pid: {self.pid} LoopCount: {count}')


if __name__ == '__main__':
    processes = []
    for i in range(2, 5):
        p = MyProcess(i)
        processes.append(p)
        p.daemon = True
        p.start()
    for p in processes:
        p.join()

print('Main Process ended')
