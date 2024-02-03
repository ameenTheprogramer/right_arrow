from pynput.keyboard import Controller, Key
import time

keyboard = Controller()

def press_right_arrow_key():
    while True:
        keyboard.press(Key.right)
        time.sleep(0.1)  # Adjust this sleep duration if needed
        keyboard.release(Key.right)
        time.sleep(5)  # Wait for 5 seconds before pressing the key again

# Example usage
press_right_arrow_key()
