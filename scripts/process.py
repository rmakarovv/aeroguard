import os
import yaml
import argparse

import numpy as np

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
    with open('/app/scripts/config.yaml', 'rb') as f:
        cfg = yaml.safe_load(f.read())

    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--savepath', type=str, default=cfg['savepath'], dest='savepath')
    parser.add_argument('-d', '--data', type=str, default=cfg['data'], dest='data')
    parser.add_argument('-cw', '--classification', type=str, default=cfg['classification'], dest='classification')
    parser.add_argument('-dw', '--detection', type=str, default=cfg['detection'], dest='detection')
    parser.add_argument('-sb', '--save_bboxes', action='store_true', dest='save_bboxes')
    parser.set_defaults(save_bboxes=False)

    args = parser.parse_args()
    
    detect = YOLO(args.detection)
    clf = YOLO(args.classification)
    path = args.data + '/'

    if args.savepath and args.save_bboxes:
        os.makedirs(args.savepath + "_bboxes/", exist_ok=True)

    pic_names = os.listdir(path)
    for pic_name in pic_names:
        print(f'Processing {pic_name}')

        img_path = path + pic_name
        detected = detect.predict(source=img_path, save=False, save_txt=False)

        box_list = detected[0].boxes.xyxy.int()

        boxes = get_boxes(box_list)
        
        if args.savepath and len(boxes) > 0:

            save_path = args.savepath + '_bboxes/'
            if not os.path.exists(save_path):
                os.makedirs(save_path)

            np.save(args.savepath + '_bboxes/' + pic_name.split('.')[0] + '.npy', np.array(boxes))
        
        for i, box in enumerate(boxes):
            cropped = tf.functional.crop(Image.open(img_path), *box)
            classified = clf.predict(cropped, save=False, save_txt=False)
            
            img_array = classified[0].plot()

            if args.savepath:
                img_to_save = Image.fromarray(img_array)
                img_to_save.save(args.savepath + '/' + f'{i}_{pic_name}')

if __name__ == '__main__':
    main()