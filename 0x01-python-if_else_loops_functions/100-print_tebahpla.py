#!/usr/bin/python3
for alpha in range(90, 64, -1):
    if alpha % 2 == 0:
        alpha += 32
    print("{}".format(chr(alpha)), end='')
