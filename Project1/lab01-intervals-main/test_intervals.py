"""Test suite to accompany intervals.py.

All of our CIS 211 projects will include unit test suites.  Some of them will be
provided to you.  Others you will write yourself, or you will be required to add
to an existing unit test suite.
"""

import unittest
import intervals

class Test_01_Intervals(unittest.TestCase):
    """Initial tests of the Interval class"""

    def test_00_can_create(self):
        """Can I create an interval from 3..5?"""
        try:
            i = intervals.Interval(3,5)
        except:
            self.fail("Unable to create Interval(3,5)")

    def test_01_oriented(self):
        """The low end of interval must not exceed the high end (test in constructor)"""
        with self.assertRaises(expected_exception=Exception):
            i = intervals.Interval(5,3)

    def test_02_membership(self):
        """Interval(m,n) contains exactly p such that m <= p <= n"""
        i = intervals.Interval(-1,1)
        self.assertFalse(i.contains(-12))
        self.assertFalse(i.contains(-2))
        self.assertTrue(i.contains(-1))
        self.assertTrue(i.contains(0))
        self.assertTrue(i.contains(1))
        self.assertFalse(i.contains(2))
        self.assertFalse(i.contains(15))

    def test_03_overlaps(self):
        """Intervals overlap if they contain any of the same elements"""
        i = intervals.Interval(1,3)
        self.assertTrue(i.overlaps(intervals.Interval(2,5)))
        self.assertFalse(i.overlaps(intervals.Interval(4,5)))
        self.assertFalse(i.overlaps(intervals.Interval(-3,0)))
        self.assertFalse(i.overlaps(intervals.Interval(12,17)))

    def test_04_equality(self):
        """Intervals are equal if they have the same low and high bound"""
        x = intervals.Interval(3,5)
        y = intervals.Interval(3,5)
        z = intervals.Interval(3,7)
        w = intervals.Interval(4,5)
        self.assertTrue(x == y)
        self.assertFalse(x == z)
        self.assertFalse(x == w)

    def test_05_bad_join(self):
        """Can't join intervals unless they overlap"""
        i = intervals.Interval(0, 3)
        j = intervals.Interval(4, 8)
        with self.assertRaises(Exception):
            k = i.join(j)

    def test_06_good_joins(self):
        """Join of overlapping intervals covers their union"""
        a = intervals.Interval(0,4)
        b = intervals.Interval(2,3)
        c = intervals.Interval(3,5)
        self.assertEqual(a.join(b), a)
        self.assertEqual(b.join(a), a)
        self.assertEqual(a.join(c), intervals.Interval(0,5))
        self.assertEqual(b.join(c), intervals.Interval(2,5))



if __name__ == "__main__":
    unittest.main(verbosity=2)





