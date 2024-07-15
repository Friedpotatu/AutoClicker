# Importing necessary libraries
import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

# Variables to control the auto-clicker
delay = 0.01  # Time delay between clicks
button = Button.left  # Mouse button to be clicked
start_stop_key = KeyCode(char='a')  # Key to start/stop auto-clicking
stop_key = KeyCode(char='b')  # Key to exit the auto-clicker

# Class to control the auto-clicking behavior using threading
class ClickMouse(threading.Thread):
    
    # Initializing the class with delay and button
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True
  
    # Method to start auto-clicking
    def start_clicking(self):
        self.running = True
        print("Auto-clicking started.")
  
    # Method to stop auto-clicking
    def stop_clicking(self):
        self.running = False
        print("Auto-clicking stopped.")
  
    # Method to exit the program
    def exit(self):
        self.stop_clicking()
        self.program_running = False
        print("Exiting program.")
  
    # Main method that runs the auto-clicking loop
    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)

# Create an instance of the mouse controller
mouse = Controller()
# Create an instance of the ClickMouse class
click_thread = ClickMouse(delay, button)
# Start the thread
click_thread.start()

# Function to handle key press events
def on_press(key):
    # Toggle start/stop auto-clicking
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    # Exit the program
    elif key == stop_key:
        click_thread.exit()
        listener.stop()

# Start the keyboard listener
with Listener(on_press=on_press) as listener:
    print("Press 'a' to start/stop auto-clicking.")
    print("Press 'b' to exit the program.")
    listener.join()
