import shutil
import os
import unittest

class TestPostprocessing(unittest.TestCase):
    def setUp(self):
        self.input_dir = "/app/tests/images_out"
        self.output_dir = "/app/tests/output_tmp"
        os.mkdir(self.output_dir)
        os.system(f"/app/scripts/postprocess {self.input_dir} {self.output_dir}/result.pdf")
    
    def test_report_is_generated(self):
        self.assertTrue(os.path.exists(os.path.join(self.output_dir, "result.pdf")))

    def test_report_not_empty(self):
        self.assertTrue(os.path.getsize(os.path.join(self.output_dir, "result.pdf")) > 0)

    def tearDown(self):
        shutil.rmtree(self.output_dir)

if __name__ == '__main__':
    log_file = '/app/logs/log_postprocessing_test.txt'
    with open(log_file, "w") as f:
        runner = unittest.TextTestRunner(f, verbosity=2)
        unittest.main(testRunner=runner)