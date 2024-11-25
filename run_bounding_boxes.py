import csv
import os
import base64
import time
from helper_functions.process_image import bounding_boxes
from misc.constants import CSV_FILENAME, FIELDNAMES


def read_image_as_base64(image_path):
    with open(image_path, "rb") as image_file:
        base64_data = base64.b64encode(image_file.read()).decode('utf-8')
        return f"data:image/jpeg;base64,{base64_data}"


def main():
    # Path to the images directory
    images_dir = os.path.expanduser("/Users/ankurduggal/Downloads/downloaded_images")
    images_to_find_bounding_boxes = [
        1564,
        1563,
        1562,
        1555,
        1552,
        1527,
        1119,
        1290,
        1551,
        1486,
        1232,
        1336,
        1269,
        1234,
        1111,
        1143,
        1142,
        1158,
        1145,
        1360,
        1144,
        1148]

    # Get list of all image files in the directory
    image_files = [
        f for f in os.listdir(images_dir) if f.lower().endswith(
            ('.png', '.jpg', '.jpeg', '.gif'))]

    # Check if the CSV file exists
    file_exists = os.path.isfile(CSV_FILENAME)

    # Initialize CSV with headers if it doesn't exist
    if not file_exists:
        with open(CSV_FILENAME, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
            writer.writeheader()
        processed_count = 0
    else:
        with open(CSV_FILENAME, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            processed_count = sum(1 for row in reader) - 1  # Subtract header row

    input_tokens = 0
    output_tokens = 0

    # Process images starting from where we left off
    for image_file in image_files[processed_count:]:
        if int(image_file[:4]) in images_to_find_bounding_boxes:
            image_path = os.path.join(images_dir, image_file)
            base64_image = read_image_as_base64(image_path)
            image_id = image_file[:4]  # Get first 4 characters of filename
            token_counts = bounding_boxes(base64_image, image_id)
            input_tokens += token_counts[0]
            output_tokens += token_counts[1]
            time.sleep(10)  # Sleep for 3 second after each analysis

    print(f"Input tokens: {input_tokens}")
    print(f"Output tokens: {output_tokens}")
    print(f"Total Cost: ${(input_tokens/1000000)*2.5 + (output_tokens/1000000)*10}")


if __name__ == "__main__":
    main()
