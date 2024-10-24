import os
import shutil
import unittest

class TestProcessing(unittest.TestCase):
    def setUp(self):
        self.input_dir = "/app/images"
        self.output_dir = "/app/tests/images_out_tmp"
        os.mkdir(self.output_dir)
        os.system("python3 /app/scripts/process.py -d {} -s {} -sb".format(self.input_dir, self.output_dir))
    
    def test_bounding_boxes_detected(self):
        self.assertTrue(len(os.listdir(self.output_dir + "_bboxes")) > 0)

    def test_images_processed(self):
        self.assertTrue(len(os.listdir(self.output_dir)) > 0)
    
    def tearDown(self):
        shutil.rmtree(self.output_dir)

if __name__ == '__main__':
    log_file = '/app/logs/log_processing_test.txt'
    with open(log_file, "w") as f:
        runner = unittest.TextTestRunner(f, verbosity=2)
        unittest.main(testRunner=runner)