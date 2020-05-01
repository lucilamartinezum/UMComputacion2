import time
import os
import signal

def handler(signal,frame):
    pass

def handlerUSR1(signal, frame):
    print("Soy el hijo2 con PID:", os.getpid(),  ":pong!\n")
    time.sleep(1)

def enviarSeñal(pid):
    os.kill(pid, signal.SIGUSR1)

def main():
    signal.signal(signal.SIGUSR1, handler)
    pid1 = os.fork()
    if pid1 == 0:
        for c in range(10):
            ppid = os.getppid()
            enviarSeñal(ppid)
            time.sleep(1)
            print("Soy el hijo 1 con pid: ", os.getpid(), ":ping!")

        print("¡Terminando!")

    elif pid1 != 0:
        pid2 = os.fork()
        if pid2 == 0:
            signal.signal(signal.SIGUSR1, handlerUSR1)
            while True:
                signal.pause()
        elif pid2 != 0:
            while True:
                signal.pause()
                enviarSeñal(pid2)

if __name__ == '__main__':
    main()

