import csv
import time
import subprocess
from ollama_pipeline import OllamaPipeline
from constants import PROMPT1, MODEL, CSV_FILENAME, FIELDNAMES


def process_image(base64_image, image_id):
    prompts = {
        "Musical": "Examine the image for any musical instruments, performances, or symbols. How do these elements reflect the cultural heritage and musical traditions of the society depicted?",
        "Architecture": "Analyze the architectural features present in the image. What do the design, materials, and style tell you about the culture's historical and aesthetic values?",
        "Clothing": "Look at the attire of the individuals in the image. How do their garments, accessories, and styles represent the cultural identity and customs of their community?",
        "Buddhist": "Identify any Buddhist symbols, practices, or figures in the image. How do these elements illustrate the influence of Buddhism on the culture shown?",
        "Food": "Observe any food items or dining scenes in the image. What can you infer about the culture's culinary traditions and their significance in social or ceremonial contexts?",
        "Greeting": "Notice how people interact in the image. What forms of greeting or social gestures are displayed, and what do they reveal about the culture's communication styles and etiquette?",
        "Beverage": "Detect any beverages or drinking customs depicted in the image. How do these elements reflect the cultural importance of certain drinks or rituals involved in their consumption?",
        "Garden": "Examine any garden or natural elements in the image. How does landscaping, plant selection, or garden design convey aspects of the culture's relationship with nature?",
        "Utensils": "Observe any tools or utensils shown in the image. What do their design and usage tell you about the technological development and daily life in the culture?",
        "Wedding": "Identify any wedding scenes or symbols. How do the depicted rituals, attire, and ceremonies illustrate the culture's matrimonial traditions and values?",
        "Tally": "Look for any tallying methods or counting tools in the image. What do these elements indicate about the culture's numerical systems or record-keeping practices?"}

    provider = "openai"
    model = "gpt-4o" if provider == "openai" else MODEL
    ollama_pipeline = OllamaPipeline(provider=provider, model=model)

    category = ollama_pipeline.analyze_image(base64_image, PROMPT1)
    print(f"Image Cateegory: {category}")
    print(f"PROMPT: {prompts[category]}")
    result = ollama_pipeline.analyze_image(base64_image, prompts[category])

    line = {'Image ID': image_id, 'Analysis Result': result, 'Status': 'Completed'}

    if provider == "ollama":
        time.sleep(1)  # Sleep for 1 second after each analysis
        # Run the shell command to stop llava:13b
        subprocess.run(["ollama", "stop", MODEL], check=True)

    # Append results to CSV after each image is processed
    with open(CSV_FILENAME, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
        writer.writerows(line)

    print(f"Results appended to {CSV_FILENAME}")
