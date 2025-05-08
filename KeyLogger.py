from pynput import keyboard
INPS = []

def on_press(key):
    global INPS
    try:
        INPS.append(key.char)
    except AttributeError:
        if key == key.space:
            INPS.append(" ")
        
        elif key == key.enter:
            INPS.append("\n")
        
        elif key == key.backspace:
            if len(INPS) != 0:
                del INPS[-1]
            pass
        
        elif key == key.tab:
            INPS.append("\t")

        elif key == key.esc:
            with open("inputs.txt", "w") as file:
                for inp in INPS:
                    file.write(inp)
                file.close()
            exit()


if __name__ == '__main__':
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
    