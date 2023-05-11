#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = len(sys.argv)
    total = sum(int(sys.argv[x]) for x in range(1, args))
    print("{}".format(total))
