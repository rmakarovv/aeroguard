import unittest

class TestPostprocessing(unittest.TestCase):
    def test_postprocessing(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    log_file = 'log_postprocessing_test.txt'
    with open(log_file, "w") as f:
        runner = unittest.TextTestRunner(f, verbosity=2)
        unittest.main(testRunner=runner)