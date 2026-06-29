import unittest
import os
import sys

# Ensure Python can locate the local development folder during testing
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import my_minipack.progress
import my_minipack.logger

class TestMyMinipack(unittest.TestCase):

    def test_imports(self):
        """Verify that submodules can be targeted and parsed successfully."""
        self.assertIsNotNone(my_minipack.progress)
        self.assertIsNotNone(my_minipack.logger)

    def test_progress_iterable(self):
        """Verify that ft_progress correctly yields elements from an iterable collection."""
        test_range = range(5)
        output = list(my_minipack.progress.ft_progress(test_range))
        self.assertEqual(output, [0, 1, 2, 3, 4])

    def test_logger_decorator(self):
        """Verify that the logger decorator can wrap a function without disrupting its return payload."""
        @my_minipack.logger.log
        def dummy_function():
            return "42AI"
        
        result = dummy_function()
        self.assertEqual(result, "42AI")

if __name__ == '__main__':
    unittest.main()
