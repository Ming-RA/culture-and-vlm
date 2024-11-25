import matplotlib.pyplot as plt
import os
import csv
import json


def show_box(box, ax):
    x0, y0 = box[0], box[1]
    w, h = box[2] - box[0], box[3] - box[1]
    ax.add_patch(plt.Rectangle((x0, y0), w, h, edgecolor='green', facecolor=(0, 0, 0, 0), lw=2))


def show_image(image, boxes_str, image_id):
    plt.figure(figsize=(10, 10))
    plt.imshow(image)

    boxes_data = json.loads(boxes_str)
    for box_data in boxes_data['boxes']:
        box = [box_data['x1'], box_data['y1'], box_data['x2'], box_data['y2']]
        show_box(box, plt.gca())
        plt.text(box_data['x1'], box_data['y1'] - 5, box_data['label'],
                 color='green', fontsize=10, bbox=dict(facecolor='white', alpha=0.7))

    plt.axis('off')
    # Create directory if it doesn't exist
    save_dir = os.path.expanduser("~/Downloads/bounding-boxes-4o-2")
    os.makedirs(save_dir, exist_ok=True)

    # Save the figure
    save_path = os.path.join(save_dir, f"{image_id}.png")
    plt.savefig(save_path, bbox_inches='tight', pad_inches=0)
    plt.close()
    plt.show()


def create_bounding_box_dict():
    bounding_boxes_dict = {}
    with open('gpt-4o_bounding_boxes.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            bounding_boxes_dict[row['Image ID']] = row['Bounding Boxes + Labels']
    return bounding_boxes_dict


def main():
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

    bounding_box_dict = create_bounding_box_dict()

    # Get list of all image files in the directory
    image_files = [
        f for f in os.listdir(images_dir) if f.lower().endswith(
            ('.png', '.jpg', '.jpeg', '.gif'))]

    for image_file in image_files:
        if int(image_file[:4]) in images_to_find_bounding_boxes:
            image_path = os.path.join(images_dir, image_file)
            image = plt.imread(image_path)
            image_id = int(image_file[:4])
            show_image(image, bounding_box_dict[str(image_id)], image_id)


if __name__ == "__main__":
    main()
