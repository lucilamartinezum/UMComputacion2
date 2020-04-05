#!/usr/bin/python

import sys
import getopt

def main():
    try:
        (opt, args) = getopt.getopt(sys.argv[1:], 'i:o:', [])
    except getopt.GetoptError as err:
        print("ERROR", str(err))
        exit()

    if len(opt) != 2:
        print("*The number of parameters and arguments is incorrect.*")
        exit()
    else:
        print("Options entered : ", opt)
    for op, arg in opt:
        if op == '-i':
            infile = arg
        else:
            pastefile = arg
    try:
        FileIn = open(infile, "r")
    except FileNotFoundError as error:
        print("The file you want to copy has not been found.")
        print(error)
        exit()
        return

    lines = FileIn.readlines()
    FileIn.close()

    FilePaste = open(pastefile, "w")
    FilePaste.writelines(lines)
    FilePaste.close()

    print("Done!")

main()