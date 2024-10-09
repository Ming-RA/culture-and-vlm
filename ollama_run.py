import csv
import pandas as pd
from ollama_pipeline import OllamaPipeline


def main():
    ollama_pipeline = OllamaPipeline()
    prompts = ["1", "2", "3", "4"]
    results = []

    # Try with 'ISO-8859-1' encoding
    try:
        with open('images.csv', 'r', encoding='ISO-8859-1') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)  # Skip header row if present

            for row in csv_reader:
                image_url = row[1]  # Get the URL from the second column
                for prompt in prompts:
                    result = ollama_pipeline.analyze_image(
                        image_url, prompt, ollama_pipeline.client)
                    results.append({'Image URL': image_url, 'Prompt': prompt,
                                   'Analysis Result': result})
    except UnicodeDecodeError:
        # If 'ISO-8859-1' doesn't work, try 'utf-8' with error handling
        with open('images.csv', 'r', encoding='utf-8', errors='ignore') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)  # Skip header row if present

            for row in csv_reader:
                image_url = row[1]  # Get the URL from the second column
                for prompt in prompts:
                    result = ollama_pipeline.analyze_image(
                        image_url, prompt, ollama_pipeline.client)
                    results.append({'Image URL': image_url, 'Prompt': prompt,
                                   'Analysis Result': result})

    # Create a DataFrame and save to CSV
    df = pd.DataFrame(results)
    df.to_csv('analysis_results.csv', index=False)


if __name__ == "__main__":
    main()
