import time
import threading
import keyboard

while True:
    # Define the keys to be pressed
    keys_to_press = ['w', 'a', 's', 'd']

    # Define the time interval between key presses (in seconds)
    key_press_interval = 0.1  # Adjust as needed

    # Flag to track the key-pressing state
    key_pressing_enabled = False

    # Function to press and release the keys in a loop
    def press_keys():
        while True:
            if key_pressing_enabled:
                for key in keys_to_press:
                    keyboard.press(key)
                time.sleep(0.05)  # Adjust the interval as needed
                for key in keys_to_press:
                    keyboard.release(key)
                time.sleep(key_press_interval - 0.05)  # Adjust the interval as needed
            else:
                time.sleep(0.1)  # Sleep when key-pressing is disabled

    # Function to toggle the key-pressing state when the 'q' key is pressed
    def toggle_key_pressing(e):
        global key_pressing_enabled
        if e.event_type == keyboard.KEY_DOWN and e.name == 'q':
            key_pressing_enabled = not key_pressing_enabled

    # Start the key-pressing thread
    key_press_thread = threading.Thread(target=press_keys)
    key_press_thread.start()

    # Register the 'q' key to toggle key-pressing
    keyboard.on_press_key('q', toggle_key_pressing)

    while True:  # Infinite loop for the entire script
        # Run the original script for 167 seconds
        time.sleep(167)
        key_pressing_enabled = False  # Pause the original script

        # Hold the 'E' key for 4 seconds
        keyboard.press('e')
        time.sleep(4)
        keyboard.release('e')

        # Resume the original script
        key_pressing_enabled = True

    time.sleep(0.1)  # Sleep at the end of the outer while loop
