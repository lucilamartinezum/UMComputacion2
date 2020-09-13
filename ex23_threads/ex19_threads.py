import getopt
import sys
import string
import random
import threading as th
import time
import os


def runProcess(r, l, file):
    letter = random.choice(string.ascii_letters)
    run_file = open(file, "a")
    l.acquire()
    for i in range(int(r)):
        time.sleep(1)
        run_file.write(letter)
        run_file.flush()
        print("Process:", os.getpid(), "letter:", letter)
    l.release()
    run_file.close()


def getOpts():
    try:
        (opts, args) = getopt.getopt(sys.argv[1:], 'n:f:r:', [])
        return opts
    except getopt.GetoptError as err:
        print('Error: ' + str(err))
        exit()

def main():

    if len(sys.argv[1:]) > 1:
        proc = 0
        file = ""
        iterations = 0
        opts = getOpts()
        for (opt, arg) in opts:
            if opt == "-n":
                proc = int(arg)
            if opt == "-f":
                file = arg
            if opt == "-r":
                iterations = int(arg)
        lock = th.Lock()
        for i in range(proc):
            p = th.Thread(target=runProcess, args=(iterations, lock, file))
            p.start()

        for i in range(proc):
            p.join()

    else:
        print("Try again")

if __name__ == "__main__":
    main()