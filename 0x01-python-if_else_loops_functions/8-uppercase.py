#!/usr/bin/python3
def uppercase(str):
    if ord(str) >= 97 and ord(str) <= 122:
        for string in range(97, 123):
            upper_str = chr(ord(string) - 32)
            print('{}'.format(upper_str))
    else:
        print('{}'.format(str))
