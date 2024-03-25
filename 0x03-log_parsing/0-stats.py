#!/usr/bin/python3
import sys
import signal

# Define a signal handler to capture Ctrl+C
def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

# Initialize variables to hold metrics
total_file_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

# Function to print statistics
def print_stats():
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

# Register signal handler for Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

# Read stdin line by line
for line in sys.stdin:
    try:
        # Split the line by space
        parts = line.split()

        # Check if the line has the expected format
        if len(parts) != 10:
            continue

        # Extract file size and status code
        file_size = int(parts[-1])
        status_code = int(parts[-2])

        # Update total file size
        total_file_size += file_size

        # Update status code count
        if status_code in status_codes:
            status_codes[status_code] += 1

        # Update line count
        line_count += 1

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()

    except ValueError:
        # Skip lines that don't match expected format
        continue

# Print final stats
print_stats()

