"""Nile.com is an e-commerce seller of physical books, e-books, and fine tea"""
from typing import List, Tuple


class RateTable:
    """Shipping rate table for one shipping method,
    e.g., USPS, UPS, International Blimp.
    Row (g, d) means we charge d dollars per gram for each
    gram up to g, and the remainder at the next rate in the
    table.
    """
    def __init__(self, rates: List[Tuple[int, float]]):
        self.rates = rates  # Table of (grams, dollars)

    def can_ship(self, grams: int) -> bool:
        """The last row in the rates table defines the limit
        on the amount we can ship by this mode.
        """
        limit_grams, last_rate = self.rates[-1]
        return grams <= limit_grams

    def cost(self, grams: int) -> float:
        """Shipping charge for n grams from our shipping rates"""
        total = 0.0
        remaining = grams
        for limit, rate in self.rates:
            portion = min(remaining, limit)
            remaining = remaining - portion
            total += portion * rate
            if remaining == 0:
                return total
        raise ValueError(f"Cannot ship {grams} grams")


class Item:
    """Something sold by Nile.com.  (Abstract class)"""

    def cost(self) -> float:
        """Cost of item, exclusive of shipping"""
        raise NotImplementedError(f"Concrete class {type(self)} must implement cost")

    def shipping_weight(self) -> int:
        """Weight in grams of this item"""
        raise NotImplementedError(f"Concrete class {type(self)} must implement shipping_weight")


class PaperBook(Item):
    """A book made from paper.  These still exist"""

    def __init__(self, title: str, price: float, weight_gr: int):
        self.title = title
        self.weight = weight_gr
        self.price = price
        # Do not add instance variables

    def __str__(self) -> str:
        return f"{self.title} (physical book)"

    def cost(self) -> float:
        return self.price

    def shipping_weight(self) -> int:
        return self.weight


class EBook(Item):
    """A book made from bits. We ship these electronically
    regardless of shipping method.
    """

    def __init__(self, title: str, price: float, unlock_code: str):
        self.title = title
        self.unlock = unlock_code
        self.price = price

    def __str__(self) -> str:
        return f"{self.title} (electronic book unlock code)"

    def cost(self) -> float:
        return self.price

    def shipping_weight(self) -> int:
        return 0


class Tea(Item):
    """We sell fine tea by the gram"""

    def __init__(self, variety: str, price_per_gram: float, grams: int):
        self.variety = variety
        self.price = price_per_gram
        self.grams = grams

    def __str__(self) -> str:
        return f"{self.grams} grams of {self.variety} tea"

    def cost(self) -> float:
        return self.grams * self.price

    def shipping_weight(self) -> int:
        return self.grams


class Cart:
    """Shopping cart (items to purchase)"""
    def __init__(self):
        self.items = []

    def add(self, item: Item):
        self.items.append(item)

    def base_cost(self) -> float:
        """Total cost of items in cart, not including shipping"""
        return sum([item.cost() for item in self.items])

    def shipping(self, rates: RateTable) -> float:
        """Determine what the cost of the whole shipment would
        be if we used this mode, e.g., DHL Overnight
        """
        return rates.cost(sum([item.shipping_weight() for item in self.items]))

    def __str__(self) -> str:
        """Price out each item, exclusive of shipping"""
        lines = [f"{str(item):50} ${item.cost():.2f}" for item in self.items]
        return "\n".join(lines)


def main():
    """Example purchase with example shipping rates"""
    cart = Cart()
    cart.add(PaperBook("Native Son", 15.00, 350))  # $15
    cart.add(EBook("Python for Humans", 35.00, "E3920382"))  # $35
    cart.add(Tea("Darjeeling Fancy Flowery", 1.00, 8))  # $1 per gram x 8 grams = $8
    cart.add(Tea("Oolong", 1.25, 4))   # $1.25 per gram x 4 grams = $5

    assert cart.base_cost() == 63.00, "Total cost should be $63 before shipping"

    usps_rates = RateTable([(10, 0.75),  # First 10 grams at 0.75/gram
                            (100, 0.50),  # Next 100 grams at 0.50/gram
                            (1000, 0.30),  # Next 1000 grams at 0.30/gram
                            (999_999, 0.25)])  # Remainder at 0.25/gram

    # Note: We ought to check whether this box is too heavy, but for simplicity we'll assume
    # that nobody buys THAT much tea.

    usps = cart.shipping(usps_rates)
    print(f"USPS shipping {usps:.2f} for")
    print(cart)


if __name__ == "__main__":
    main()
