#!/usr/bin/python
from os import getpid, fork, getppid
from sys import argv
from getopt import getopt

def main():
    (opts, args) = getopt(argv[1:], "n:")
    numberChild = 0
    for(opt, arg) in opts:
        if opt == '-n':
            numberChild = int(arg)
            print("Cantidad de procesos hijos:", numberChild, "\n")
    for c in range(numberChild):
        createChild = fork()
        if createChild == 0:
            talk()

def talk():
    idprocceschild = getpid()
    idfather = getppid()
    print("Soy el proceso", idprocceschild, "y mi padre es", idfather)
    exit()

main()
