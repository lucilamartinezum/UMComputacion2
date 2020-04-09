#!/usr/bin/python

import sys
import getopt
import subprocess
import datetime

def main():
    try:
        (opts, args) = getopt.getopt(sys.argv[1:], 'c:f:l:', [])
    except getopt.GetoptError as err:
        print("***ERROR: The loading of options and arguments has not been respected***", str(err))
        exit()

    if len(opts) != 3:
        print("***The number of parameters and arguments is incorrect.***")
        print("OPTIONS ENTERED: error arises >>> ", opts)
        exit()
    else:
        print("Correct entered options:>>> ", opts)
        exit()

    command = " "
    output_file = " "
    log_file = " "
    for opt, arg in opts:
        if opt == "-c":
            command = arg
        elif opt == "-f":
            output_file = open(arg, "a")
        elif opt == "-l":
            log_file = open(arg, "a")
    process = subprocess.Popen([command], stdout=output_file, stderr=subprocess.PIPE, shell=True, universal_newlines=True)
    error = process.communicate()[1]
    if not error:
        log_file.write(str(datetime.datetime.now()) + " Command " + command + "It has been executed correctly.")
        output_file.write("\n")
    else:
        log_file.write(str(datetime.datetime.now()) + ">>" + str(error))
    output_file.close()
    log_file.close()

main()


