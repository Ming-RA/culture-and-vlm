import csv
import os
import base64
import time
from helper_functions.process_image import process_image
from misc.constants import CSV_FILENAME, FIELDNAMES


def read_image_as_base64(image_path):
    with open(image_path, "rb") as image_file:
        base64_data = base64.b64encode(image_file.read()).decode('utf-8')
        return f"data:image/jpeg;base64,{base64_data}"


def main():
    # Path to the images directory
    images_dir = os.path.expanduser("/Users/ankurduggal/Downloads/downloaded_images")
    images_to_be_processed = [1527, 1234, 1362, 1339, 1306, 1270,
                              1297, 1500, 1143, 1137, 1459, 1554, 1204, 1184, 1360, 1448]

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

    # Process images starting from where we left off
    for image_file in image_files[processed_count:]:
        if int(image_file[:4]) in images_to_be_processed:
            image_path = os.path.join(images_dir, image_file)
            base64_image = read_image_as_base64(image_path)
            image_id = image_file[:4]  # Get first 4 characters of filename
            process_image(base64_image, image_id)
            time.sleep(10)  # Sleep for 3 second after each analysis


if __name__ == "__main__":
    main()
