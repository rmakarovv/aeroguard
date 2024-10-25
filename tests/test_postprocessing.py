import os
import shutil
import unittest

class TestPostprocessing(unittest.TestCase):
    def setUp(self):
        self.cwd = os.getcwd()
        self.input_dir = os.path.join(self.cwd, "tests/images_out")
        self.output_dir = os.path.join(self.cwd, "tests/output_tmp")
        os.mkdir(self.output_dir)
        os.system(f"{os.path.join(self.cwd, 'scripts/postprocess')} {self.input_dir} {self.output_dir}/result.pdf")
    
    def test_report_is_generated(self):
        self.assertTrue(os.path.exists(os.path.join(self.output_dir, "result.pdf")))

    def test_report_not_empty(self):
        self.assertTrue(os.path.getsize(os.path.join(self.output_dir, "result.pdf")) > 0)

    def tearDown(self):
        shutil.rmtree(self.output_dir)

if __name__ == '__main__':
    log_file = os.path.join(os.getcwd(), 'logs/log_postprocessing_test.txt')
    with open(log_file, "w") as f:
        runner = unittest.TextTestRunner(f, verbosity=2)
        unittest.main(testRunner=runner)