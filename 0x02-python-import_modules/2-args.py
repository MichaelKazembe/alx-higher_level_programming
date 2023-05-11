#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_len = len(sys.argv) - 1
    x = arg_len

    if x == 0:
        print("{} arguments.".format(x))
    elif x == 1:
        print("{} argument:".format(x))
    else:
        print("{} arguments:".format(x))

    if x >= 1:
        for i in range(1, arg_len + 1):
            print("{}: {}".format(i, sys.argv[i]))
