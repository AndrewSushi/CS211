"""
Closed intervals of integers
Andrew Chan, 2022-03-29, CIS 211
"""

class Interval:
    def __init__(self, low: int, high: int):
        self.low = low
        self.high = high
        if (low > high):
            raise ValueError

    def contains(self, i: int) -> bool:
        return (self.low <= i <= self.high)

    def overlaps(self, other: "Interval") -> bool:
        if (other.low > self.high):
            return False
        elif (other.high < self.low):
            return False
        return True

    def __eq__(self, other: "Interval") -> bool:
        return (self.low == other.low) and (self.high == other.high)

    def join(self, other: "Interval") -> "Interval":
        assert(self.overlaps(other))
        return Interval(min(self.low, other.low), max(self.high, other.high))