import unittest

class TestProcessing(unittest.TestCase):
    def test_processing(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    log_file = 'log_processing_test.txt'
    with open(log_file, "w") as f:
        runner = unittest.TextTestRunner(f, verbosity=2)
        unittest.main(testRunner=runner)