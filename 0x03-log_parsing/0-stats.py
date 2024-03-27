#!/usr/bin/python3

import sys

def print_msg(status_codes, total_file_size):
    """
    Print statistics of status codes and total file size.
    
    Args:
        status_codes (dict): Dictionary containing status codes and their counts.
        total_file_size (int): Total size of the files.
    """
    print("Total File Size: {}".format(total_file_size))
    for code, count in sorted(status_codes.items()):
        if count != 0:
            print("{}: {}".format(code, count))

total_file_size = 0
status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

try:
    for line in sys.stdin:
        parsed_line = line.split()  # Split the line into tokens
        parsed_line = parsed_line[::-1]  # Reverse the order of tokens

        if len(parsed_line) > 2:
            total_file_size += int(parsed_line[0])  # Update total file size
            code = parsed_line[1]  # Get status code from the line

            if code in status_codes:
                status_codes[code] += 1  # Increment count for the status code

            if total_file_size % 10 == 0:  # Print statistics every 10 lines
                print_msg(status_codes, total_file_size)
                status_codes = {code: 0 for code in status_codes}  # Reset counts
                total_file_size = 0  # Reset total file size

finally:
    print_msg(status_codes, total_file_size)  # Print final statistics

