import multiprocessing as mp
import getopt
import sys


def split_list(alist, wanted_parts):
    length = len(alist)
    return [alist[i * length // wanted_parts: (i + 1) * length // wanted_parts] for i in range(wanted_parts)]


def calculate(numbers, values):
    for number in numbers:
        values.append(number ** 2)


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
    list_range = list(range(num_min, num_max))
    splited_list = split_list(list_range, process)
    list_process = list()
    manager = mp.Manager()
    values = manager.list()
    for i in range(process):
        list_process.append(mp.Process(target=calculate, args=(splited_list[i], values,)))
    for proceso in list_process:
        proceso.start()
    for proceso in list_process:
        proceso.join()
    print('These are the resulting squares:')
    print(values)


if __name__ == "__main__":
    main()
