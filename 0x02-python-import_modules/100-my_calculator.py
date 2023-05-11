#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    args = len(sys.argv) - 1
    args1 = "./100-my_calculator.py"

    if args < 4:
        print("Usage: {} <a> <operator> <b>".format(args1))
    else:
        a = int(sys.argv[1])
        operator = sys.argv[2]
        b = int(sys.argv[3])

        if operator == "+":
            print("{} + {} = {}".format(a, b, add(a, b)))
        elif operator == "-":
            print("{} - {} = {}".format(a, b, sub(a, b)))
        elif operator == "*":
            print("{} * {} = {}".format(a, b, mul(a, b)))
        elif operator == "/":
            print("{} / {} = {}".format(a, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
