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
        response = requests.get(image_url)
        return base64.b64encode(response.content).decode('utf-8')

    def analyze_image(self, image_url, prompt, client):
        base64_image = self.encode_image_from_url(image_url)
        response = client.chat.completions.create(
            model="llava:13b-v1.6-vicuna-fp16",
            messages=[
                {
                    "role": "system",
                    "content": "You are a culturally aware assistant who will help with any task.."
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
