#!/usr/bin/python3
"""
Defining script that reads
stdin line by line and computes metrics.
"""

import sys


def compute_metrics():
    """
    Reads input from stdin, computes metrics, and prints the results.

    Parameters:
    - None

    Returns:
    - None
    """

    file_size = 0
    status_tally = {
            "200": 0, "301": 0, "400": 0, "401": 0,
            "403": 0, "404": 0, "405": 0, "500": 0}
    line_count = 0

    try:
        for line in sys.stdin:
            tokens = line.split()
            if len(tokens) >= 2:
                status_code = tokens[-2]
                if status_code in status_tally:
                    status_tally[status_code] += 1

                try:
                    file_size += int(tokens[-1])
                except ValueError:
                    pass

            line_count += 1

            if line_count % 10 == 0:
                print("File size: {:d}".format(file_size))
                for key, value in sorted(status_tally.items()):
                    if value:
                        print("{:s}: {:d}".format(key, value))

        print("File size: {:d}".format(file_size))
        for key, value in sorted(status_tally.items()):
            if value:
                print("{:s}: {:d}".format(key, value))

    except KeyboardInterrupt:
        print("File size: {:d}".format(file_size))
        for key, value in sorted(status_tally.items()):
            if value:
                print("{:s}: {:d}".format(key, value))


compute_metrics()
