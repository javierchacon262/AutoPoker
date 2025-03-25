import mss
import numpy as np
import cv2
import time
import pyautogui

print("Move your mouse to the top-left of the poker table and press Enter.")
input()
x1, y1 = pyautogui.position()

print("Move your mouse to the bottom-right of the poker table and press Enter.")
input()
x2, y2 = pyautogui.position()

def capture_screen(region, save_path="./screenshots/"):
    """Captura una imagen de la mesa de póker y la guarda."""
    with mss.mss() as sct:
        screenshot = sct.grab(region)
        img = np.array(screenshot)
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        filename = f"{save_path}poker_{int(time.time())}.png"
        cv2.imwrite(filename, img)
        print(f"Imagen guardada: {filename}")

# Define la región de la mesa en la pantalla (ajústala manualmente)
region = {"top": y1, "left": x1, "width": x2-x1, "height": y2-y1}

# Capturar 1 imagen cada 5 segundos por 30 minutos (~360 imágenes por sesión)
for _ in range(360):
    capture_screen(region)
    time.sleep(5)
