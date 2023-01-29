class Fraction:
    def __init__(self, num: int, den: int):
        assert num > 0 or den >= 0, "AssertionError: Denominator cannot be 0 and Numerator cannot be negative "
        self.num = num
        self.den = den

    def __str__(self) -> str:
        return f"{self.num}/{self.den}"
        
    def __repr__(self) -> str:
        pass

f1 = Fraction(6,8)
f2 = Fraction(4,0)
f3 = Fraction(-3,4)
