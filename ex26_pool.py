import multiprocessing as mp
import getopt
import sys
import os


def split_list(alist, wanted_parts):
    length = len(alist)
    return [alist[i * length // wanted_parts: (i + 1) * length // wanted_parts] for i in range(wanted_parts)]


def calculate(number):
    print("Pool worker PID", os.getpid(), "calculating...")
    return number ** 2

def getOpts():
    try:
        (opts, args) = getopt.getopt(sys.argv[1:], 'p:m:n:', [])
        return opts
    except getopt.GetoptError as err:
        print('Error: ' + str(err))
        exit()


opts = getOpts()

for (opt, arg) in opts:
    if opt == "-p":
        process = int(arg)
    elif opt == "-m":
        num_min = int(arg)
    elif opt == "-n":
        num_max = int(arg)


def main():
    pool = mp.Pool()
    list_range = list(range(num_min, num_max))
    splited_list = split_list(list_range, process)
    for values in splited_list:
        map_f = (pool.map(calculate, values))
        print("These are the resulting squares:", map_f)

    print("-------------------------------------")

    for values in splited_list:
        apply_f = [pool.apply(calculate, args=(i,)) for i in values]
        print("These are the resulting squares:", apply_f)

    pool.close()


if __name__ == "__main__":
    main()