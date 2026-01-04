import pyautogui
from datetime import datetime

def take_screenshot():
    # Create filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"screenshot_{timestamp}.png"

    # Take screenshot
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)

    print(f"Screenshot saved as {filename}")

if __name__ == "__main__":
    take_screenshot()
