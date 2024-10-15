import csv
import os
from process_image import process_image
from constants import CSV_FILENAME


def main():

    # Check if the CSV file exists
    file_exists = os.path.isfile(CSV_FILENAME)

    if file_exists:
        with open(CSV_FILENAME, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            row_count = sum(1 for row in reader)
    else:
        row_count = 0

    # Try with 'ISO-8859-1' encoding
    with open('images.csv', 'r', encoding='ISO-8859-1') as csv_file:
        csv_reader = csv.reader(csv_file)
        for i in range((row_count // 3) + 1):
            next(csv_reader)  # Skip rows already processed

        for row in csv_reader:
            image_url = row[1]  # Get the URL from the second column
            process_image(image_url)


if __name__ == "__main__":
    main()
