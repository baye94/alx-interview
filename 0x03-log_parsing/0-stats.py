#!/usr/bin/python3
import sys

status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
total_size = 0
line_count = 0

for line in sys.stdin:
    line_count += 1
    try:
        ip, date, request, status, file_size = line.split(" ")
        status = int(status)
        file_size = int(file_size)
    except ValueError:
        continue

    if status in status_codes:
        status_codes[status] += 1

    total_size += file_size

    if line_count % 10 == 0:
        print("File size: {}".format(total_size))
        for code in sorted(status_codes):
            if status_codes[code] > 0:
                print("{}: {}".format(code, status_codes[code]))
