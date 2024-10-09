import csv
import pandas as pd
from ollama_pipeline import OllamaPipeline


def main():
    ollama_pipeline = OllamaPipeline()
    prompts = [
        """Observe the image carefully and deconstruct the details that may reveal cultural influences. Don’t restrict your thinking to just traditional markers—consider a wide range of visual, contextual, and symbolic elements. Use these guiding questions to spark insight, but feel free to think beyond them:

	1.	Visual Style and Design Aesthetics: What overall style does the image convey? Is the composition minimalistic, ornate, geometric, or organic? How might this reflect cultural design philosophies or artistic movements?
	2.	Physical Environment: Where does the image seem to be set? Look at the geography, climate, and any natural or urban elements. Is it in a bustling city, rural village, desert, mountains, or tropical area? Could these environmental clues hint at a specific culture?
	3.	Cultural Symbols and Iconography: Are there any prominent symbols, icons, or visual metaphors? These could be religious, political, or ideological. How do these symbols interact with cultural narratives or historical contexts?
	4.	Postures, Gestures, and Expressions: What are the people doing with their bodies? Are they engaging in a particular type of movement, dance, or gesture? What do their expressions and body language suggest about social norms, emotions, or roles within their cultural context?
	5.	Food, Objects, and Daily Life: Are there any foods, utensils, or everyday objects depicted? How do these reflect cultural dietary habits, technologies, or economic conditions?
	6.	Cultural Innovation and Fusion: Does the image contain elements that feel like a blend of different cultures, or signs of cultural exchange, innovation, or hybridization? How do these elements work together, and what cultures do they appear to be combining?
	7.	Cultural Values and Philosophies: What emotions, values, or philosophies seem to be conveyed? Is there a sense of community, individuality, spirituality, or materialism? How might these align with broader cultural attitudes or ideologies?
	8.	Historical or Temporal Context: Does the image appear rooted in a particular time period? What historical clues (such as style of dress, technology, or architecture) hint at cultural evolution or historical significance?
	9.	Color, Light, and Mood: Consider the use of colors, light, and shadows. Some cultures associate particular colors or lighting with specific meanings or emotions—how might these choices be reflective of cultural attitudes or storytelling techniques?
	10.	Abstract or Conceptual Elements: Are there any abstract qualities—like rhythm, harmony, or tension—within the image? What emotions or ideas are being evoked? Think about how these could resonate with cultural expressions in art, literature, or philosophy.

Take your time to interpret these layers holistically and look for subtle connections or juxtapositions. Culture is multifaceted, so think beyond the obvious and consider the image as a dynamic blend of history, tradition, innovation, and social context."""]
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
                    print(f"Analysis completed for image: {image_url}")
                    results.append({'Image URL': image_url, 'Prompt': prompt,
                                   'Analysis Result': result, 'Status': 'Completed'})
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
                    print(f"Analysis completed for image: {image_url}")
                    results.append({'Image URL': image_url, 'Prompt': prompt,
                                   'Analysis Result': result})

    # Create a DataFrame and save to CSV
    df = pd.DataFrame(results)
    df.to_csv('analysis_results.csv', index=False)


if __name__ == "__main__":
    main()
