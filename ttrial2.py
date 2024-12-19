import time
import win32gui
import psutil
import os
import sys
import time
import win32gui
import win32process
import psutil
# Ensure the script supports UTF-8 output


# List of keywords to check in the window title

arr =["hey " "bye"]

def get_active_window_title():
    hwnd = win32gui.GetForegroundWindow()  # Get the handle to the active window
    if hwnd:
        return win32gui.GetWindowText(hwnd)  # Get the title of the window
    return None


def get_process_id(hwnd):
    """Get the process ID for a given window handle."""
    _, pid = win32process.GetWindowThreadProcessId(
        hwnd)  # Use win32process here
    return pid


def close_app(pid):
    """Terminate the application with the given process ID."""
    try:
        process = psutil.Process(pid)
        print(f"Closing application: {process.name()} (PID: {pid})")
        process.terminate()
    except Exception as e:
        print(f"Error closing application: {e}")


if __name__ == "__main__":
    try:
        print("Monitoring active windows. Press Ctrl+C to stop.")
        while True:
            hwnd = win32gui.GetForegroundWindow()  # Get the handle to the active window
            title = get_active_window_title()  # Get the active window's title

            if title:
                for keyword in keywords:
                    if keyword.lower() in title.lower():  # Check if any keyword is in the title
                        print(f"Keyword '{keyword}' found in title '{
                              title}'. Closing app...")
                        # Get the process ID of the app
                        pid = get_process_id(hwnd)
                        close_app(pid)  # Close the app
                        break
            time.sleep(5)  # Check every 5 seconds
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")
