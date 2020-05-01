import sys
import getopt
import signal
import time
import os

def handlerUSR2(sig, frame):
    print("Soy el proceso con PID: ", os.getpid(), "recibí la señal SIGUSR2", sig, "de mi padre PID:", os.getppid())

def enviarSeñal(pid):
    pid = int(pid)
    os.kill(pid, signal.SIGUSR2)

def main():
    (opts, args) = getopt.getopt(sys.argv[1:], 'p:', ['process='])
    if len(opts) < 2:
        print("\nEspecifique cuantos procesos hijos desea crear usando: -p <num> o --process <num>")
    for option, value in opts:
        if option == "-p" or option == "--process":
            childs = int(value)

            for c in range(childs):
                child = os.fork()
                if child == 0:
                    signal.signal(signal.SIGUSR2, handlerUSR2)
                    signal.pause()
                    os._exit(0)
                else:
                    time.sleep(1)
                    print("Creando proceso. PID: ", child,"\n")
                    enviarSeñal(child)
                    os.wait()
                    print("¡Listo!")

if __name__ == '__main__':
    main()
