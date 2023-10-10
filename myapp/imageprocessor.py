import cv2
import numpy as np
import os

def process_image(image):
    # Construct the full file path by joining 'media/' with the image file name
    media_path = os.path.join('media/', image)
    # Load the image using OpenCV
    image_cv2 = cv2.imread(media_path)

    # Define the coordinates and dimensions of the color boxes on the strip
    # This is an example; you should adjust these values based on your image
    box_coordinates = [
        (122, 42, 70, 60),  # URO box
        (10, 60, 40, 90),  # BIL box
        (10, 110, 40, 140),  # KET box
        (10, 160, 40, 190),  # BLD box
        (10, 210, 40, 240),  # PRO box
        (10, 260, 40, 290),  # NIT box
        (10, 310, 40, 340),  # LEU box
        (122, 662, 62, 54),  # GLU box
        (10, 410, 40, 440),  # SG box
        (10, 460, 40, 490),  # PH box
    ]

    # Initialize a dictionary to store the identified colors
    color_identification_results = {}

    for idx, (x, y, w, h) in enumerate(box_coordinates):
        # Crop the region of interest (a color box)
        color_box = image_cv2[y:y + h, x:x + w]

        # Calculate the average color in the color box
        average_color = np.mean(color_box, axis=(0, 1)).astype(int)

        # Assign a color label based on the box's position (e.g., 'URO', 'BIL', etc.)
        color_label = get_color_label(idx)

        # Store the identified color in the results dictionary
        color_identification_results[color_label] = average_color.tolist()

    return color_identification_results


def get_color_label(box_index):
    # This function assigns a color label based on the box's position.
    # Modify this logic based on your specific color box layout.
    if box_index == 0:
        return 'URO'
    elif box_index == 1:
        return 'BIL'
    elif box_index == 2:
        return 'KET'
    elif box_index == 3:
        return 'BLD'
    elif box_index == 4:
        return 'PRO'
    elif box_index == 5:
        return 'NIT'
    elif box_index == 6:
        return 'LEU'
    elif box_index == 7:
        return 'GLU'
    elif box_index == 8:
        return 'SG'
    elif box_index == 9:
        return 'PH'

    return 'Unknown'
