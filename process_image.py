import csv
import time
import subprocess
from ollama_pipeline import OllamaPipeline
from constants import PROMPT1, PROMPT2, PROMPT3, MODEL, CSV_FILENAME, FIELDNAMES


def process_image(image_url):
    ollama_pipeline = OllamaPipeline()
    prompts = [PROMPT1, PROMPT2, PROMPT3]
    image_results = []
    for i, prompt in enumerate(prompts):
        result = ollama_pipeline.analyze_image(image_url, prompt)
        print(f"Analysis completed for prompt {i+1}")
        image_results.append({'Image URL': image_url, 'Prompt': prompt,
                             'Analysis Result': result, 'Status': 'Completed'})
        time.sleep(5)  # Sleep for 5 seconds after each analysis

    # Run the shell command to stop llava:13b
    subprocess.run(["ollama", "stop", MODEL], check=True)

    # Append results to CSV after each image is processed
    with open(CSV_FILENAME, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
        writer.writerows(image_results)

    print(f"Results appended to {CSV_FILENAME}")

    return image_results
