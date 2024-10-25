import os
import shutil
import unittest

class TestProcessing(unittest.TestCase):
    def setUp(self):
        self.cwd = os.getcwd()
        self.input_dir = os.path.join(self.cwd, "tests/images")
        self.output_dir = os.path.join(self.cwd, "tests/images_out_tmp")
        os.mkdir(self.output_dir)
        os.system(f"python3 {os.path.join(self.cwd, 'scripts/process.py')} -d {self.input_dir} -s {self.output_dir} -sb")
    
    def test_bounding_boxes_detected(self):
        self.assertTrue(len(os.listdir(self.output_dir + "_bboxes")) > 0)

    def test_images_processed(self):
        self.assertTrue(len(os.listdir(self.output_dir)) > 0)
    
    def tearDown(self):
        shutil.rmtree(self.output_dir)

if __name__ == '__main__':
    log_file = os.path.join(os.getcwd(), 'logs/log_processing_test.txt')
    with open(log_file, "w") as f:
        runner = unittest.TextTestRunner(f, verbosity=2)
        unittest.main(testRunner=runner)