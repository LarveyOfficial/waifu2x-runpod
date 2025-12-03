import runpod
import requests
import torch
import base64
from io import BytesIO
from PIL import Image

def download_image(url, filename):
    """
    Downloads an image from a given URL and saves it to a specified filename.

    Args:
        url (str): The URL of the image to download.
        filename (str): The name of the file to save the image as.
    """
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"Image downloaded successfully to {filename}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading image: {e}")


def pil_image_to_base64(image_object, format="PNG"):
    """
    Converts a PIL.Image.Image object to a Base64 encoded string.

    Args:
        image_object (PIL.Image.Image): The PIL Image object to convert.
        format (str): The image format to use for saving (e.g., "PNG", "JPEG").

    Returns:
        str: The Base64 encoded string of the image.
    """
    buffered = BytesIO()
    image_object.save(buffered, format=format)
    img_byte = buffered.getvalue()
    img_str = base64.b64encode(img_byte).decode("utf-8")
    return img_str

def handler(event):
    print(f"Worker Start")
    prompt_input = event['input']

    image = prompt_input.get('image')
    method = prompt_input.get('method', 'scale')
    noise_level = prompt_input.get('noise_level', -1)

    download_image(image, 'input_image.jpg')

    model = torch.hub.load("nagadomi/nunif:master", "waifu2x",
                           method=method, noise_level=noise_level, trust_repo=True).to("cuda")


    input_image = Image.open("input_image.jpg")
    result = model.infer(input_image)

    base64_string = pil_image_to_base64(result, format="PNG")

    formated_output = 'data:image/png;base64,' + base64_string

    return formated_output



runpod.serverless.start({"handler": handler})