import pyautogui

print("Move your mouse to the top-left of the poker table and press Enter.")
input()
x1, y1 = pyautogui.position()

print("Move your mouse to the bottom-right of the poker table and press Enter.")
input()
x2, y2 = pyautogui.position()

print(f"Screen capture coordinates: {x1}, {y1}, {x2
}, {y2}")