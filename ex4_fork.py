#!/usr/bin/python
from os import getpid, fork, wait

def main():

    child = fork()
    if child:
        idprocess = getpid()
        print('Soy el padre, PID:', idprocess, 'mi hijo es', child)
        print('Soy el padre, PID:', idprocess, 'mi hijo es', child)
        wait()
        print('Mi proceso hijo, PID:', child, 'termino.')
    else:
        imp5timesChild()
        print('Hijo PID', getpid(), "terminando...\n")

def imp5timesChild():
    for c in range(5):
        print("Soy el hijo, PID", getpid())
    return

main()