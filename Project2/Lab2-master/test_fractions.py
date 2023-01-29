"""Test suite to accompany fractions.py.

All of our CIS 211 projects will include unit test suites.  Some of them will be
provided to you.  Others you will write yourself, or you will be required to add
to an existing unit test suite.
"""

import unittest
import fractions

class Test_01_Fraction(unittest.TestCase):
    """Initial tests of the Fraction class"""

    def test_00_can_create(self):
        """Can I create an fraction of 6/8?"""
        try:
            i = fractions.Fraction(6, 8)
        except:
            self.fail("Unable to create Fraction(6,8)")

    def test_01_oriented(self):
        """Neither the numerator nor the denominator can be < 0 and the denominator cannot be <= 0"""
        with self.assertRaises(expected_exception=Exception):
            i = fractions.Fraction(-3, 4)
            i = fractions.Fraction(4, 0)

    def test_02_str(self):
        """Magic method is used whenever you print an object"""
        a = fractions.Fraction(5, 8)
        self.assertEqual(a.__str__(), '5/8')
        b = fractions.Fraction(1, 2)
        self.assertEqual(b.__str__(), '1/2')

    def test_03_repr(self):
        """A string that looks like a call to the constructor of the class"""
        i = fractions.Fraction(3, 8)
        self.assertEqual(i.__repr__(), 'Fraction(3, 8)')

    def test_04_mul(self):
        """multiply both the fractions"""
        a = fractions.Fraction(3, 4)
        self.assertTrue(__eq__(a.__mul__(fractions.Fraction(2, 5)), fractions.Fraction(6, 20)))

    def test_05_add(self):
        """Adding both the fractions"""
        a = fractions.Fraction(3, 4)
        self.assertTrue(__eq__(a.__add__(fractions.Fraction(2, 5)), fractions.Fraction(23, 20)))

    def test_06_simplify(self):
        """simplifying the fractions"""
        a = fractions.Fraction(35, 56)
        self.assertTrue(__eq__(a, fractions.Fraction(5, 8)))


def __eq__(a: "Fraction", b: "Fraction") -> "Fraction":
    """Intervals are equal if they have the same low and high bounds"""
    return a.num == b.num and a.den == b.den


if __name__ == "__main__":
    unittest.main(verbosity=2)