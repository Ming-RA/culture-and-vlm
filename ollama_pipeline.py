import base64
import requests
from openai import OpenAI


class OllamaPipeline:

    def __init__(self):
        self.client = OpenAI(
            base_url='http://localhost:11434/v1',
            api_key='ollama',  # required, but unused
        )

    def encode_image_from_url(self, image_url):
        try:
            response = requests.get(image_url)
            response.raise_for_status()  # This will raise an exception for HTTP errors
            return base64.b64encode(response.content).decode('utf-8')
        except requests.RequestException as e:
            print(f"Error fetching image from URL: {e}")
            return None

    def analyze_image(self, image_url, prompt):
        base64_image = self.encode_image_from_url(image_url)
        if base64_image is None:
            return "Unable to process the image due to an error with the provided URL."

        response = self.client.chat.completions.create(
            model="llava:13b-v1.6-vicuna-fp16",
            messages=[
                {
                    "role": "system",
                    "content": "You are a culturally aware assistant who will help with any task."
                },
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            },
                        },
                    ],
                }
            ],
        )
        return response.choices[0].message.content
