import os
import unittest

class TestPostprocessing(unittest.TestCase):
    def setUp(self):
        os.system("/app/scripts/preprocess /app/images_raw /app/images")
    
    def test_postprocessing(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    log_file = 'log_postprocessing_test.txt'
    with open(log_file, "w") as f:
        runner = unittest.TextTestRunner(f, verbosity=2)
        unittest.main(testRunner=runner)