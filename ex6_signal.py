from os import fork, wait, kill, getpid
from signal import pause, signal, SIGUSR1, SIGINT
import time

def handlerUSR1(sig, frame):
    print("***Soy el hijo y recibí la señal USR1 de padre***")

def handlerINT(sig, frame):
    pid = getpid()
    killChild(pid)
    time.sleep(2)
    print("El usuario ha interrumpido el proceso padre con la señal INT. ¡¡¡Cerrando!!! ")
    exit()

def killChild(pid):
    sigpid =pid+1
    kill(sigpid, 9)

def child():
    while True:
        print("¡¡¡Soy el hijo y estoy esperando!!!")
        pause()

def main():
    signal(SIGUSR1, handlerUSR1)
    signal(SIGINT, handlerINT)
    pid = fork()
    if pid == 0:
        print("Proceso hijo iniciando:" +str(getpid()))
        child()
    else:
        print("Soy el padre, PID: "+str(getpid()))
        for c in range(10):
            time.sleep(5)
            kill(pid, SIGUSR1)
        time.sleep(1)
        print("Proceso padre matando al hijo",pid,"...")
        kill(pid, 15)
        print("Proceso padre PID: ",getpid(), "terminando...")

if __name__ == '__main__':
    main()