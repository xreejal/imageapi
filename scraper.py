from dotenv import load_dotenv
load_dotenv()

import os
import requests
import time
from PIL import Image
from io import BytesIO
import base64
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
IMG_SIZE = (1024, 1024)

def download_image(url_or_path):
    """Download an image from a URL or load from a local file path."""
    try:
        if url_or_path.startswith("http"):
            response = requests.get(url_or_path)
            response.raise_for_status()
            img = Image.open(BytesIO(response.content))
        else:
            img = Image.open(url_or_path)
        return img.convert("RGB")
    except Exception as e:
        raise ValueError(f"Failed to load image from {url_or_path}: {e}")

def preprocess_image(img, size=IMG_SIZE):
    """Resize an image to the specified size."""
    return img.resize(size, Image.Resampling.LANCZOS)

def encode_image_to_base64(img):
    """Encode a PIL image to a base64 string."""
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

def save_image(img, path):
    """Save an image to the specified file path."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    img.save(path)
    return path

def call_dalle_api(prompt):
    """Make a request to OpenAI's DALL·E API to generate an image from a prompt."""
    try:
        print(f"Sending prompt (length: {len(prompt)}): {prompt[:200]}...")
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt[:4000],  # Ensure prompt isn't too long
            n=1,
            size=f"{IMG_SIZE[0]}x{IMG_SIZE[1]}",
            quality="standard",
            style="vivid",
            response_format="url"
        )
        img_url = response.data[0].url
        img = download_image(img_url)
        return img
    except Exception as e:
        print(f"Full error details: {dir(e)}")
        if hasattr(e, 'response'):
            print(f"Response content: {e.response.text}")
        raise RuntimeError(f"API call failed: {e}")

def test_api():
    """Test the API connection with a simple prompt."""
    try:
        test_prompt = "A simple red apple on a white table"
        img = call_dalle_api(test_prompt)
        img.show()
        return True
    except Exception as e:
        print(f"API test failed: {e}")
        return False

def generate_composite_image(reference_images, instruction, output_path="output/generated_image.png"):
    """Generate a composite image using DALL·E API based on reference images and instructions."""
    try:
        if not test_api():
            raise RuntimeError("API test failed, not proceeding with main request")

        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # Verify all reference images exist
        for img_path in reference_images:
            download_image(img_path)  # Will raise error if fails

        time.sleep(20)  # Rate limiting

        result_img = call_dalle_api(instruction)
        save_image(result_img, output_path)
        img_b64 = encode_image_to_base64(result_img)

        return output_path, img_b64

    except Exception as e:
        print(f"Error during generation: {str(e)}")
        return None, None

if __name__ == "__main__":
    reference_images = [
        "https://as1.ftcdn.net/v2/jpg/02/36/99/22/1000_F_236992283_sNOxCVQeFLd5pdqaKGh8DRGMZy7P4XKm.jpg",
        "https://as2.ftcdn.net/v2/jpg/03/03/62/45/1000_F_303624505_u0bFT1Rnoj8CMUSs8wMCwoKlnWlh5Jiq.jpg",
        "https://plus.unsplash.com/premium_photo-1694819488591-a43907d1c5cc?fm=jpg&q=60&w=3000",
        "https://hips.hearstapps.com/hmg-prod/images/gettyimages-1094874726.png?crop=1.00xw:0.753xh;0,0.161xh&resize=1200:*"
    ]

    instruction = (
        "Create a cinematic fantasy landscape with: "
        "1. The shot composition from the first reference image "
        "2. Characters from the other images in similar poses "
        "3. Background from the last image "
        "4. Vivid sunset lighting and colors"
    )

    output_path, img_b64 = generate_composite_image(reference_images, instruction)

    if output_path:
        print(f"Image saved to: {output_path}")
    if img_b64:
        print(f"Base64 (first 100 characters): {img_b64[:100]}...")