import os
import sys
import signal
import time

def handlerUSR2_A(signal, frame):
    print("Proceso A (PID=%d) leyendo:\n" % os.getpid())

def handlerUSR1_B(signal, frame):
    print("Mensaje 1 (PID=%d)\n" % os.getpid())

def handlerUSR1_C(signal, frame):
    print("Mensaje 2 (PID=%d)\n" % os.getpid())

def main():
    r, w = os.pipe()
    child = os.fork()

    if not child:
        signal.signal(signal.SIGUSR1, handlerUSR1_B)
        gppid = os.getppid()
        signal.pause()

        os.close(r)
        gc = os.fork()
        if not gc:
            signal.signal(signal.SIGUSR1, handlerUSR1_C)
            signal.pause()
           #proceso C escribe mensaje 2
            message = "Mensaje 2 (PID=" + str(os.getpid()) + ")\n"

            with os.fdopen(w, 'w') as w:
                w.write(message)
                w.close()

            time.sleep(2)
            os.kill(gppid, signal.SIGUSR2)

            os._exit(0)
        else:
            message = "Mensaje 1 (PID=" + str(os.getpid()) + ")\n"
            # Proceso B escribe mensaje 1
            with open(w, 'w') as w:
                w.write(message)
                w.flush()

            time.sleep(2)
            os.kill(gc, signal.SIGUSR1)

    else:
        signal.signal(signal.SIGUSR2, handlerUSR2_A)
        time.sleep(2)
        os.kill(child, signal.SIGUSR1)
        signal.pause()

    #proceso A realiza lectura
        os.close(w)
        with open(r, 'r') as r:
            while True:
                line = r.readline()
                if line:
                    print(line)
                else:
                    break
            r.close()

        os.wait()
        os._exit(0)

if __name__ == '__main__':
    main()




