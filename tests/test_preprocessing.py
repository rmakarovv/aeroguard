import os
import shutil
import unittest

import cv2

def includes_all_from_first(list1, list2):
    for el in list1:
        if el not in list2:
            return False
    return True

class TestPreprocessing(unittest.TestCase):
    def setUp(self):
        self.cwd = os.getcwd()
        self.input_path = os.path.join(self.cwd, "tests/images_raw")
        self.output_path = os.path.join(self.cwd, "tests/images_tmp")
        os.mkdir(self.output_path)
        os.system(f"{os.path.join(self.cwd, 'scripts/preprocess')} {self.input_path} {self.output_path}")
        self.files_raw = os.listdir(self.input_path)
        self.files_out = os.listdir(self.output_path)
    
    def test_images_convertation(self):
        self.assertTrue(includes_all_from_first(self.files_raw, self.files_out), msg="Some of the input images were not processed")

    def test_images_are_close(self):
        noise_ok = []
        for fname in self.files_raw:
            img_raw = cv2.imread(os.path.join(self.input_path, fname), cv2.IMREAD_GRAYSCALE)
            img_out = cv2.imread(os.path.join(self.output_path, fname), cv2.IMREAD_GRAYSCALE)
            img_size = img_raw.shape[0] * img_raw.shape[1]
            noise_ok.append(cv2.norm(img_raw, img_out) < 0.1 * img_size)
        self.assertTrue(all(noise_ok), msg="Some of the images are not close enough to the input")

    def tearDown(self):
        shutil.rmtree(self.output_path)

if __name__ == '__main__':
    log_file = os.path.join(os.getcwd(), 'logs/log_preprocessing_test.txt')
    with open(log_file, "w") as f:
        runner = unittest.TextTestRunner(f, verbosity=2)
        unittest.main(testRunner=runner)