import time  # Importing time to use sleep function
import pygetwindow as gw  # For interacting with window titles


def close_window_if_title_contains(arr):
    while True:  # Start an infinite loop
        for window in gw.getAllTitles():  # Get all open window titles
            try:
                # Print the window title
                print(f"Checking window title: {window}")

                # Check if the window title contains any word from arr
                if any(word.lower() in window.lower() for word in arr):
                    # Print the title before closing
                    print(f"Found matching window title: {window}")
                    gw.getWindowsWithTitle(
                        window)[0].close()  # Close the window
            except Exception as e:
                print(f"Error: {e}")
        time.sleep(2)  # Wait for 5 seconds before checking again


# List of words to match against window titles
arr = ['hello', 'hey', 'bye']
close_window_if_title_contains(arr)
