from transformers import pipeline, AutoModelForImageTextToText, AutoProcessor
import torch
import cv2
from PIL import Image

# Define the local path to the model directory
model_path = "./gemma_local/"

processor = AutoProcessor.from_pretrained(model_path, use_fast=True)
model     = AutoModelForImageTextToText.from_pretrained(model_path)

# Initialize the pipeline
pipe = pipeline(
    "image-text-to-text",
    model=model,
    processor=processor,
    device="mps" if torch.backends.mps.is_available() else "cpu",
    torch_dtype=torch.bfloat16
)



# Load the image using OpenCV
opencv_image = cv2.cvtColor(cv2.imread("Screenshot 2024-10-01 at 21.28.47.png"), cv2.COLOR_BGR2RGB)

# Convert the OpenCV image (BGR) to PIL format (RGB)
pil_image = Image.fromarray(opencv_image)

# Define the input message
messages = [
    {
        "role": "system",
        "content": [{"type": "text", "text": "You are a helpful assistant."}]
    },
    {
        "role": "user",
        "content": [{"type": "text", "text": "Describe the image in detail."}]
    },
    {
        "role": "system",
        "content": [{ "type": "image", "image": pil_image}]
    }
]

#processed_inputs = processor(messages, return_tensors="pt").to(model.device)

# Generate the response
output = pipe(text=messages, images=[pil_image], max_new_tokens=200)
print(output[0]["generated_text"][-1]['content'])

