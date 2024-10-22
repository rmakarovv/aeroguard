import os
import torch
import yaml

import numpy as np
import torchvision as tv

from matplotlib import pyplot as plt

from ultralytics import YOLO
from PIL import Image
from torchvision import transforms as tf


def get_boxes(boxes_list):
    
    boxes = []

    for i, row in enumerate(boxes_list):
        x_min, y_min, x_max, y_max = row

        width = x_max - x_min
        height = y_max - y_min

        boxes.append([y_min.item(), x_min.item(), height.item(), width.item()])

    return boxes


def main():
    
    with open('config.yaml', 'rb') as f:
        cfg = yaml.safe_load(f.read())
    
    detect = YOLO(cfg['detection'])
    clf = YOLO(cfg['classification'])
    path = cfg['data'] + '/'

    pic_name = np.random.choice(os.listdir(path)) # the picture is chosen randomly

    print(pic_name)

    img_path = path + pic_name
    detected = detect.predict(source=img_path, save=False, save_txt=False)

    box = detected[0].boxes.xyxy.int()

    boxes = []
    for i, row in enumerate(box):
        x_min, y_min, x_max, y_max = row

        width = x_max - x_min
        height = y_max - y_min

        boxes.append([y_min.item(), x_min.item(), height.item(), width.item()])
    
    for i, box in enumerate(boxes):
        cropped = tf.functional.crop(Image.open(img_path), *box)
        classified = clf.predict(cropped, save=False, save_txt=False)
        
        img_array = classified[0].plot()

        if cfg['savepath']:
            img_to_save = Image.fromarray(img_array)
            img_to_save.save(cfg['savepath'] + '/' + f'{i}_{pic_name}')

if __name__ == '__main__':
    main()