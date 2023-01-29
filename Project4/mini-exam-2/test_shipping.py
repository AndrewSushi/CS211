"""Test cases (just 2!) for shipping.py"""

import unittest
from shipping import *

class TestNileCarts(unittest.TestCase):
    """Test Nile.com shopping cart calculations"""

    def setUp(self) -> None:
        cart = Cart()
        cart.add(PaperBook("Native Son", 15.00, 350))  # $15
        cart.add(EBook("Python for Humans", 35.00, "E3920382"))  # $35
        cart.add(Tea("Darjeeling Fancy Flowery", 1.00, 8))  # $1 per gram x 8 grams = $8
        cart.add(Tea("Oolong", 1.25, 4))  # $1.25 per gram x 4 grams = $5
        self.cart = cart

    def test_base_cost_calc(self):
        """Total cost should be $63.00 before shipping"""
        self.assertEqual(self.cart.base_cost(), 63.00)

    def test_shipping_cost(self):
        """Shipping cost is based on the total cost of all the physical items, treating
        virtual items like e-books as if they had zero weight.
        """
        usps_rates = RateTable([(10, 0.75),  # First 10 grams at 0.75/gram
                                        (100, 0.50),  # Next 100 grams at 0.50/gram
                                        (1000, 0.30),  # Next 1000 grams at 0.30/gram
                                        (999_999, 0.25)])
        usps_shipping = self.cart.shipping(usps_rates)  # Remainder at 0.25/gram
        self.assertEqual(usps_shipping, 133.10)

if __name__ == "__main__":
    unittest.main()
