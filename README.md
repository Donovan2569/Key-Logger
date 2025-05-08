# Key-Logger
Personal computer key logger to learn how to capture user input.

# Legal Disclaimer
This project is intended for educational and personal use only. Unauthorized installation or use of this software on any device that you do not own or have explicit permission to monitor is both illegal and unethical, and may violate local, state, and federal laws.
The author assumes no responsibility for any misuse, damage, or legal consequences resulting from the use of this software.

# Features
1. Captures keystrokes in real-time
2. Supports logging of special keys like Enter, Backspace, etc.
3. Saves logs to a file (e.g "keys.txt")

# Requirements
1. Python 3.x
2. `pynput` library 
    - Install via: 
    ```bash
     pip install pynput
     ```

# Usage
1. Clone the repository:
    ```bash
    git clone https://github.com/Donovan2569/Key-Logger.git
    cd key-logger
    ```
2. Run the keylogger
    - python keylogger.py
3. Check the output file
    - When 'esc' is pressed all inputs will be dumped into 'keys.txt'