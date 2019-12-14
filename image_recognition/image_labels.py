import io
import os
from google.cloud import vision
from google.cloud.vision import types

def get_image_labels(image_url):
    client = vision.ImageAnnotatorClient()
    file_name = os.path.abspath(image_url)

    with io.open(image_url, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.label_detection(image=image)
    return response.label_annotations