import openai
import base64
from utils.config import AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_KEY, AZURE_OPENAI_DEPLOYMENT

def analyze_with_vision(image):
    openai.api_base = AZURE_OPENAI_ENDPOINT
    openai.api_key = AZURE_OPENAI_KEY
    openai.api_type = "azure"
    openai.api_version = "2024-02-01"

    with open(image, "rb") as img_file:
        image_bytes = img_file.read()

    base64_img = base64.b64encode(image_bytes).decode()

    messages = [
        {"role": "system", "content": "You are an expert at interpreting engineering diagrams and operation instructions."},
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Extract the step-by-step 'Sequence of Operation' from this image. Return a clean, structured list of steps."},
                {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{base64_img}"}}
            ]
        }
    ]

    response = openai.ChatCompletion.create(
        model=AZURE_OPENAI_DEPLOYMENT,
        messages=messages,
        max_tokens=1000
    )

    return response.choices[0].message["content"]
