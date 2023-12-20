#!/usr/bin/python3
"""Log Parser"""
import sys


class LogParser:
    def __init__(self):
        self.file_size = 0
        self.status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                             403: 0, 404: 0, 405: 0, 500: 0}

    def print_stats(self):
        """ Print statistics """
        print('File size: {}'.format(self.file_size))
        for key in sorted(self.status_codes.keys()):
            if self.status_codes[key]:
                print('{}: {}'.format(key, self.status_codes[key]))

    def parse_line(self, line):
        """ Checks the line for matches """
        try:
            line = line.rstrip()
            words = line.split(' ')
            # File size is the last parameter on stdout
            self.file_size += int(words[-1])
            # Status code comes before file size
            status_code = int(words[-2])
            # Move through the dictionary of status codes
            if status_code in self.status_codes:
                self.status_codes[status_code] += 1
        except (ValueError, IndexError):
            pass

    def process_logs(self):
        linenum = 1
        try:
            for line in sys.stdin:
                self.parse_line(line)
                """ print after every 10 lines """
                if linenum % 10 == 0:
                    self.print_stats()
                linenum += 1
        except KeyboardInterrupt:
            self.print_stats()
            raise
        self.print_stats()


if __name__ == '__main__':
    log_parser = LogParser()
    log_parser.process_logs()
