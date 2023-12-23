# Import necessary libraries
import pyfiglet
import sys
import socket
from datetime import datetime
import configparser

# Load configuration from config.ini
config = configparser.ConfigParser()
config.read('config.ini')

# Get configuration values
socket_timeout = float(config.get('JvckScanConfig', 'socket_timeout'))
start_port = int(config.get('JvckScanConfig', 'start_port'))
end_port = int(config.get('JvckScanConfig', 'end_port'))

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

# Scan every port on the target IP using the configured range
try:
    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(socket_timeout)

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
