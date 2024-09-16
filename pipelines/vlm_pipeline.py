import base64
from openai import OpenAI
from gradio_client.client import Client
from gradio_client.utils import handle_file


client = OpenAI()


class VLM_Pipeline:
    def __init__(self, client):
        self.client = client

    def encode_image(self, image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    def analyze_image(self, image_path, prompt, client):
        match client:

            case "openai":
                base64_image = self.encode_image(image_path)

                response = client.chat.completions.create(
                    model="gpt-4o-2024-08-06",
                    messages=[
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

            case "qwen2":
                client = Client("Qwen/Qwen2-VL")

                # First, add the image file
                result = client.predict(
                    history=[],
                    file=handle_file(image_path),
                    api_name="/add_file"
                )

                # Then, add the text prompt
                result = client.predict(
                    history=result,
                    text=prompt,
                    api_name="/add_text"
                )

                return result
