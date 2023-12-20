#!/usr/bin/python3
"""Log Parser"""


import sys
from collections import defaultdict

def print_stats(total_size, status_counts):
    print("File size: {}".format(total_size))
    for status_code in sorted(status_counts.keys()):
        count = status_counts[status_code]
        print("{}: {}".format(status_code, count))

def parse_line(line):
    try:
        parts = line.split()
        ip_address = parts[0]
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        return ip_address, status_code, file_size
    except (ValueError, IndexError):
        return None, None, None

def main():
    total_size = 0
    status_counts = defaultdict(int)
    try:
        for i, line in enumerate(sys.stdin, start=1):
            ip_address, status_code, file_size = parse_line(line.strip())
            if ip_address is not None:
                total_size += file_size
                status_counts[status_code] += 1

            if i % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)


if __name__ == "__main__":
    main()
