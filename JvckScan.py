# Import necessary libraries
import pyfiglet
import sys
import socket
from datetime import datetime

# Create and print custom banner (optional)
ascii_banner = pyfiglet.figlet_format("JvckScan")
print(ascii_banner)

# Create target variable to store input for target IP
# Make a string for easier formatting
target = input("Input Target IP: ")

# Create information banner
# Include timestamp
print("_" * 50)
print(f"Scanning Target: {target}")
print("Scanning started at: " + str(datetime.now()))
print("_" * 50)

# Scan every port on the target IP (1 - 65535)
try:
    for port in range(1, 65536):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        # Return open ports
        result = s.connect_ex((target, port))
        if result == 0:
            print("[*] Port {} is open".format(port))
        s.close()

# Catch keyboard interrupts
except KeyboardInterrupt:
    print("\nExiting JvckScan :(")
    sys.exit()

# Catch socket errors
except socket.error:
    print("Host not responding :(")
    sys.exit()
