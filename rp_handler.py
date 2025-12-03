import runpod
import requests
import torch
import base64
from io import BytesIO
from PIL import Image

def download_image(url, filename):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"Image downloaded successfully to {filename}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading image: {e}")


def pil_png_to_base64(image_object):
    buffered = BytesIO()
    image_object.save(buffered, format="PNG")
    img_byte = buffered.getvalue()
    img_str = base64.b64encode(img_byte).decode("utf-8")
    return img_str

def handler(event):
    print(f"Worker Start")
    prompt_input = event['input']

    image = prompt_input.get('image')
    model_type = prompt_input.get('model_type', 'art')
    method = prompt_input.get('method', 'scale')
    noise_level = prompt_input.get('noise_level', -1)
    tile_size = prompt_input.get('tile_size', 256)
    batch_size = prompt_input.get('batch_size', 4)
    keep_alpha = prompt_input.get('keep_alpha', True)
    amp = prompt_input.get('amp', True)

    download_image(image, 'input_image.jpg')

    model = torch.hub.load("nagadomi/nunif:master", "waifu2x",
                           model_type=model_type,
                           method=method,
                           noise_level=noise_level,
                           trust_repo=True,
                           tile_size=tile_size,
                           batch_size=batch_size,
                           keep_alpha=keep_alpha,
                           amp=amp).to("cuda")


    input_image = Image.open("input_image.jpg")
    result = model.infer(input_image)

    base64_string = pil_png_to_base64(result)

    formated_output = 'data:image/png;base64,' + base64_string

    return formated_output


runpod.serverless.start({"handler": handler})