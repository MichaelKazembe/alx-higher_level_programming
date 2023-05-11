#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = len(sys.argv)
    for arguments in range(1, arg):
        print("{}: {}".format(arguments, sys.argv[arguments]))
    if arg <= 1:
        print("{} arguments.".format(arg - 1))
    elif arg == 2:
        print("{} argument:\n{}:".format(arg - 1, sys.argv[1]))
    else:
        print("{} arguments:\n{}:".format(arg - 1, join(sys.argv[1:])))
