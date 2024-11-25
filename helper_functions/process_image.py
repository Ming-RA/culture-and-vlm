import csv
import time
import io
import base64
import subprocess
from PIL import Image
from helper_functions.pipeline import Pipeline
from misc.constants import PROMPT1, PROMPTS, PROMPT2, MODEL, CSV_FILENAME, FIELDNAMES, BOUNDING_BOX_PROMPTS


def process_image(base64_image, image_id):

    provider = "openai"
    model = "gpt-4o"
    ollama_pipeline = Pipeline(provider=provider, model=model)

    category = ollama_pipeline.analyze_image(base64_image, PROMPT1).strip()
    print(f"Image Cateegory: {category}")
    print(f"PROMPT: {PROMPTS[category]}")
    result = ollama_pipeline.analyze_image(base64_image, PROMPTS[category]).strip()
    culture = ollama_pipeline.analyze_image(base64_image, PROMPT2, messages=[
                                            {"role": "user", "content": result}]).strip()

    line = {
        'Image ID': image_id,
        'Category': category,
        'Analysis Result': result,
        'Culture': culture}

    if provider == "ollama":
        time.sleep(1)  # Sleep for 1 second after each analysis
        # Run the shell command to stop llava:13b
        subprocess.run(["ollama", "stop", MODEL], check=True)

    # Append results to CSV after each image is processed
    with open(CSV_FILENAME, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
        writer.writerow(line)

    print(f"Results appended to {CSV_FILENAME}")


def bounding_boxes(base64_image, image_id):
    # Get image dimensions
    image_data = base64.b64decode(base64_image.split(',')[1])
    img = Image.open(io.BytesIO(image_data))
    width, height = img.size

    provider = "openai"
    model = "gpt-4o"
    ollama_pipeline = Pipeline(provider=provider, model=model)

    category = ollama_pipeline.analyze_image(base64_image, PROMPT1).strip()
    print(f"Image Cateegory: {category}")

    # Format the prompt with actual image dimensions
    formatted_prompt = BOUNDING_BOX_PROMPTS[category].format(width=width, height=height)
    print(f"PROMPT: {formatted_prompt}")

    result = ollama_pipeline.find_bounding_boxes(base64_image, formatted_prompt).strip()

    line = {
        'Image ID': image_id,
        'Category': category,
        'Bounding Boxes + Labels': result}

    if provider == "ollama":
        time.sleep(1)
        subprocess.run(["ollama", "stop", MODEL], check=True)

    with open(CSV_FILENAME, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
        writer.writerow(line)

    print(f"Results appended to {CSV_FILENAME}")
