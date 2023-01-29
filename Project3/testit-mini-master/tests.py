"""Unit tests for testme.py"""

import unittest
from buggy import *

class TestMaxRun(unittest.TestCase):

    def test_max_run_example(self):
        self.assertEqual(max_run([1, 2, 2, 2, 3]), [2, 2, 2])
    
    def test_max_run_at_end(self):
        self.assertEqual(max_run([1, 2, 2]), [2, 2]) # If the max run was at the end

    def test_lists_only(self):
        self.assertEqual(max_run([[],[],[]]),[[],[],[]]) # If the max run are lists

if __name__ == "__main__":
    unittest.main()

