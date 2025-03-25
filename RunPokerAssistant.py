import mss
import numpy as np
import cv2
import time
import torch
import pyautogui
from pynput import keyboard
from transformers import pipeline, AutoModelForImageTextToText, AutoProcessor
from PIL import Image

# Define the local path to the model directory
model_path = "./gemma_local/"

processor = AutoProcessor.from_pretrained(model_path, use_fast=True)
model     = AutoModelForImageTextToText.from_pretrained(model_path)

messages  = []

# Initialize the pipeline
pipe = pipeline(
    "image-text-to-text",
    model=model,
    processor=processor,
    device="mps" if torch.backends.mps.is_available() else "cpu",
    torch_dtype=torch.bfloat16
)


# Screen capturing functionality
def capture_screen(regionxy, save_path="./screenshots/"):
    """Capture an image of the defined region and save it."""
    with mss.mss() as sct:
        screenshot = sct.grab(regionxy)
        img = np.array(sct.grab(regionxy))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # Convert the OpenCV image (BGR) to PIL format (RGB)
        img = Image.fromarray(img)
        #filename = f"{save_path}poker_{int(time.time())}.png"
        #cv2.imwrite(filename, img)
        #print(f"Screenshot saved: {filename}")
        return img


def define_table_region():
    """Manually define the poker table region by selecting screen coordinates."""
    print("Move your mouse to the top-left of the poker table and press Enter.")
    input()
    x1, y1 = pyautogui.position()

    print("Move your mouse to the bottom-right of the poker table and press Enter.")
    input()
    x2, y2 = pyautogui.position()

    # Return the region as a dictionary
    region = {"top": y1, "left": x1, "width": x2 - x1, "height": y2 - y1}
    print(f"Region defined: {region}")
    return region


# ------------------------------------------------------------------------------
# Función para generar respuesta del modelo
# ------------------------------------------------------------------------------
def generate_response(image=None, max_new_tokens=1024):
    # Define the input message

    messages.append({
            "role": "system",
            "content": [{"type": "image", "image": image}]
        })

    # Generate the response
    output = pipe(text=messages, images=[image], max_new_tokens=200)
    print(output[0]["generated_text"][-1]['content'])
    return output[0]["generated_text"][-1]['content']


def start_manual_screenshot(region):
    """Start listening for a key press to take a screenshot."""
    print("Press 's' to take a screenshot, or 'q' to quit.")

    def on_press(key):
        try:
            if key.char == "s":  # Press "s" to save a screenshot

                # Captura la imagen
                image    = capture_screen(region)
                # Genera la respuesta del modelo.
                response = generate_response(image=image)
                # Add the actual response to the message history
                messages.append(
                    {
                        "role": "assistant", "content": [{"type": "text", "text": response}]
                    }
                )
                # User feedback related to the response
                feedback = input("\n\n text feedback: \n\n")
                # append user feedback to the conversation
                messages.append(
                    {
                        "role": "user", "content": [{"type": "text", "text": feedback}]
                    }
                )
                # Next hand message append
                messages.append(
                    {
                        "role": "user", "content": [{"type": "text", "text": "Lets continue with the next hand, What's the best decision for **oldjacs** the user in the top center of the table? Your answer should be 1 single word (CALL, CHECK, RAISE, FOLD)"}]
                    }
                )

            elif key.char == "q":  # Press "q" to quit
                print("Exiting...")
                return False  # Stop the listener
        except AttributeError:
            pass  # Ignore non-character keys

    # Start listening for keys
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


if __name__ == "__main__":

    # Define poker table region
    region = define_table_region()

    #First message on the conversation with Gemma
    messages.append({"role": "system", "content": [{"type": "text", "text": "You are an expert poker player"}]})

    messages.append({
            "role": "user",
            "content": [{"type": "text",
                         "text": "Analyze the situation in silence, What's the best decision for **oldjacs** the user in the top center of the table? Your answer should be 1 single word (CALL, CHECK, RAISE, FOLD)"}]
        })

    # Start manual screenshot process
    start_manual_screenshot(region)

