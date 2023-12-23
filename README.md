# JvckScan - Simple Port Scanner

## Overview

JvckScan is a lightweight Python script designed for scanning open ports on a target IP address. This tool facilitates a quick assessment of a host's security posture by identifying accessible ports within the entire range (1 to 65535).

## Features

- **User-Friendly Interface:** JvckScan prompts the user to input the target IP address, making it easy to initiate scans.
  
- **Port Scanning:** The script utilizes socket programming to scan each port within the specified range and identifies open ports on the target.

- **Informative Output:** Results are displayed in the console, providing a clear indication of open ports on the target IP.

## Usage

1. Run the script by executing the Python file.

   python jvckscan.py

2. Input the target IP address when prompted.

3. The script will initiate a port scan and display the results.

## Dependencies

Ensure you have the following Python libraries installed:

pip install pyfiglet

## Notes

- JvckScan is designed for educational and informational purposes.
- Use responsibly and ensure compliance with applicable laws and regulations.

## License

This project is licensed under the [MIT License](LICENSE).
