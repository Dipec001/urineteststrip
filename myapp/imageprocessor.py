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
        (124, 42, 64, 58),  # URO box
        (124, 134, 64, 57),  # BIL box
        (120, 216, 70, 62),  # KET box
        (124, 300, 68, 58),  # BLD box
        (120, 392, 66, 58),  # PRO box
        (124, 474, 64, 62),  # NIT box
        (122, 575, 64, 58),  # LEU box
        (122, 662, 62, 54),  # GLU box
        (118, 748, 68, 60),  # SG box
        (118, 834, 66, 64),  # PH box
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
