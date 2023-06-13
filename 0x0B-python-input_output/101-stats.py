#!/usr/bin/python3

"""
a script that reads stdin line by line and computes metrics

"""

import sys


def print_metrics(total_size, status_codes):
    """Prints the metrics"""
    print("File size: {}".format(total_size))
    sorted_codes = sorted(status_codes.keys())
    for code in sorted_codes:
        count = status_codes[code]
        print("{}: {}".format(code, count))


def compute_metrics():
    """Computes the metrics"""
    total_size = 0
    status_codes = {}

    try:
        line_count = 0
        for line in sys.stdin:
            line = line.strip()
            if line:
                parts = line.split(" ")
                size = int(parts[-1])
                status_code = parts[-2]

                total_size += size

                if status_code in status_codes:
                    status_codes[status_code] += 1
                else:
                    status_codes[status_code] = 1

                line_count += 1

                if line_count % 10 == 0:
                    print_metrics(total_size, status_codes)
    except KeyboardInterrupt:
        print_metrics(total_size, status_codes)


compute_metrics()
