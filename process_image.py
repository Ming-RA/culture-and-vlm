import csv
import time
import subprocess
from ollama_pipeline import OllamaPipeline
from constants import PROMPT1, PROMPTS, PROMPT2, MODEL, CSV_FILENAME, FIELDNAMES


def process_image(base64_image, image_id):

    provider = "gemini"
    model = "gemini-1.5-flash-002"
    ollama_pipeline = OllamaPipeline(provider=provider, model=model)

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
