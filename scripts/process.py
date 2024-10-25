"""
This module implements an object detection and classification pipeline using YOLO models.

It provides functionality to load configuration settings, process input images for object
detection, and classify the detected objects. The results, including bounding boxes and
classified images, can be saved to specified paths.

Usage:
    python process.py --savepath <save_directory> --data <input_images_directory> 
                     --classification <classification_model> 
                     --detection <detection_model> --save_bboxes

Dependencies:
    - os: Standard library for interacting with the operating system.
    - argparse: Standard library for parsing command-line arguments.
    - yaml: PyYAML library for reading YAML configuration files.
    - numpy: Library for numerical computations, especially for handling arrays.
    - ultralytics: YOLO implementation for object detection and classification.
    - PIL (Pillow): Python Imaging Library for opening, manipulating, and saving image files.

"""

import os
import argparse
import yaml

import numpy as np

from ultralytics import YOLO
from PIL import Image
from torchvision import transforms as tf


def get_boxes(box_tens):
    """
    Convert a tensor of bounding boxes of format (x_min, y_min, x_max, y_max)
    to a list of boxes in (y_min, x_min, height, width) format.

    Parameters:
    box_tens (torch.tensor): A tensor of bounding boxes, where each row corresponds
                             to bounding box box is consisting of four elements:
                             [x_min, y_min, x_max, y_max].

    Returns:
    list: A list of converted bounding boxes, where each box is represented
          as [y_min, x_min, height, width].
    """

    boxes = []  # Initialize an empty list to store converted bounding boxes

    # Iterate over each row in the input tensor
    for _, row in enumerate(box_tens):
        # Unpack the coordinates of the bounding box
        x_min, y_min, x_max, y_max = row

        # Calculate width and height of the bounding box
        width = x_max - x_min
        height = y_max - y_min

        # Append the converted box format [y_min, x_min, height, width] to the list
        boxes.append([y_min.item(), x_min.item(), height.item(), width.item()])

    return boxes


def main():
    """
    Main entry point for the object detection and classification pipeline.

    This function loads configuration from a YAML file or parses command-line
    arguments, and processes images for object detection and classification.
    Detected bounding boxes can be saved as NumPy arrays, and classified defects
    can be saved as cropped versions of the original images with modified filenames.

    Command-Line Arguments:
        -s, --savepath: Path for saving results (default from config).
        -d, --data: Directory containing input images (default from config).
        -cw, --classification: Path to the classification model (default from config).
        -dw, --detection: Path to the detection model (default from config).
        -sb, --save_bboxes: Flag to save detected bounding boxes.
    """

    with open("/app/scripts/config.yaml", "rb") as config_file:
        cfg = yaml.safe_load(config_file.read())

    # Set up argument parsing for command-line options
    parser = argparse.ArgumentParser()

    # Argument for specifying the save path for results
    parser.add_argument(
        "-s", "--savepath", type=str, default=cfg["savepath"], dest="savepath"
    )

    # Argument for the input data directory containing images
    parser.add_argument("-d", "--data", type=str, default=cfg["data"], dest="data")

    # Argument for the path to the classification model
    parser.add_argument(
        "-cw",
        "--classification",
        type=str,
        default=cfg["classification"],
        dest="classification",
    )

    # Argument for the path to the detection model
    parser.add_argument(
        "-dw", "--detection", type=str, default=cfg["detection"], dest="detection"
    )

    # Flag for saving detected bounding boxes as NumPy files
    parser.add_argument("-sb", "--save_bboxes", default=False, action="store_true", dest="save_bboxes")
    # parser.set_defaults(save_bboxes=False)

    # Argument parsing
    args = parser.parse_args()

    # Initialize YOLO models for detection and classification
    detect = YOLO(args.detection)
    clf = YOLO(args.classification)
    path = args.data + "/"

    # Create a directory for saving bounding boxes if specified
    if args.savepath and args.save_bboxes:
        os.makedirs(args.savepath + "_bboxes/", exist_ok=True)

    # List all image files in the specified data directory
    pic_names = [oic for pic in os.listdir(path) if not pic.startswith('.')]
    for pic_name in pic_names:
        print(f"\n --- Processing {pic_name} ---")

        # Construct the full path for the current image
        img_path = path + pic_name

        # Perform detection on the current image
        detected = detect.predict(source=img_path, save=False, save_txt=False)

        # Retrieve the bounding boxes from the detection results
        box_tens = detected[0].boxes.xyxy.int()

        # Convert bounding box tensor to a boxes list
        boxes = get_boxes(box_tens)

        # Save bounding boxes to a specified directory if required
        if args.savepath and args.save_bboxes and len(boxes) > 0:
            np.save(
                args.savepath + "_bboxes/" + pic_name.split(".")[0] + ".npy",
                np.array(boxes),
            )

        # Iterate over each detected bounding box for classification
        for i, box in enumerate(boxes):
            cropped = tf.functional.crop(Image.open(img_path), *box)
            classified = clf.predict(cropped, save=False, save_txt=False)

            img_array = classified[0].plot()

            if args.savepath:
                img_to_save = Image.fromarray(img_array)
                img_to_save.save(args.savepath + "/" + f"{i}_{pic_name}")


if __name__ == "__main__":
    main()
