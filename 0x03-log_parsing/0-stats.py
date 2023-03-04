#!/usr/bin/python3
"""Reads stdin line by line and computes metrics"""

import sys
codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
         "404": 0, "405": 0, "500": 0}

counter = 0
file_size = 0


def printCodes(dict, file_size):
    """ Prints the status code """
    print("File size: {:d}".format(file_size))
    for i in sorted(dict.keys()):
        if dict[i] != 0:
            print("{}: {:d}".format(i, dict[i]))


try:
    for line in sys.stdin:
        if counter != 0 and counter % 10 == 0:
            printCodes(codes, file_size)

        codeList = line.split()
        counter += 1

        try:
            file_size += int(codeList[-1])
        except:
            pass

        try:
            if codeList[-2] in codes:
                codes[codeList[-2]] += 1
        except:
            pass
    printCodes(codes, file_size)


except KeyboardInterrupt:
    printCodes(codes, file_size)
    raise
