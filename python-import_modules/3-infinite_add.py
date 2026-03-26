#!/usr/bin/python3
import sys
if __name__ == "__main__":
    k = 0
    for n in range(0, len(sys.argv)):
        k = k + int(sys.argv[n])
    print("{}".format(k))
