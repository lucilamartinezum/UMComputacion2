import multiprocessing as mp
import os
import time


def child_action(proc, q):
    print('Proceso %d, PID: %d' % (proc, os.getpid()))
    time.sleep(proc)
    q.put(str(os.getpid()) + "\t")

def main():
    q = mp.Queue()
    child = []
    for c in range(10):
        j = c + 1
        process = mp.Process(target=child_action, args=(j, q,))
        child.append(process)
        child[c].start()
        child[c].join()
    print("\nCola:\n")
    while not q.empty():
        print(q.get(), end='')

    print("\nProcesos hijos terminados, padre terminando")

if __name__ == '__main__':
    main()