#!/usr/bin/python3
for first_digit in range(0, 10):
    for sec_digit in range(first_digit + 1, 10):
        if first_digit == 8:
            print("{}{}".format(first_digit, sec_digit))
            break
        print("{}{}".format(first_digit, sec_digit), end=", ")
