#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            num = 32
        else:
            num = 0
        char_ascii = ord(char)
        print("{:c}".format(char_ascii - num), end='')
    print()
