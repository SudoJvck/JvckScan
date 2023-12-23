# JvckScan - Simple Port Scanner

JvckScan is a lightweight Python script designed for scanning open ports on a target IP address. With a user-friendly interface, it prompts the user to input a target IP and initiates a scan across the configured range of ports.

## Features

- **Custom Banner:** Display a custom ASCII banner using the `pyfiglet` library.
  
- **Port Scanning:** The script utilizes socket programming to scan each port within the configured range and identifies open ports on the target.

- **Informative Output:** Results are displayed in the console, providing a clear indication of open ports on the target IP.

## Usage

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/SudoJvck/jvckscan.git
   cd jvckscan
   ```

2. **Install Dependencies:**
   ```bash
   pip install pyfiglet
   ```

3. **Run the Script:**
   ```bash
   python jvckscan.py
   ```

4. **Input Target IP:**
   Enter the target IP address when prompted.

5. **Review Results:**
   The script will initiate a port scan and display the results.

## Configuration

Adjust the script behavior by modifying the `config.ini` file.

```ini
[JvckScanConfig]
socket_timeout = 0.5
start_port = 1
end_port = 65535
```

## Notes

- JvckScan is designed for educational and informational purposes.
- Use responsibly and ensure compliance with applicable laws and regulations.

## License

This project is licensed under the [MIT License](LICENSE).
