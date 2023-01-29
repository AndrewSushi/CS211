def gcd(a, b) -> int:
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a
        return a

class Fraction:
    def __init__(self, num: int, den: int):
        if num < 0 or den <= 0:
            raise AssertionError("Denominator cannot be 0 and Numerator cannot be negative")
        self.num = num
        self.den = den
        self.simplify()

    def __str__(self) -> str:
        return f"{self.num}/{self.den}"

    def __repr__(self) -> str:
        return f"Fraction({self.num}, {self.den})"

    def __mul__(self, other: "Fraction") -> "Fraction":
        return Fraction((self.num * other.num),(self.den * other.den))

    def __add__(self, other) -> "Fraction":
        num1 = self.num * other.den
        num2 = other.num * self.den
        den1 = self.den * other.den
        return Fraction((num1 + num2), den1)

    def simplify(self) -> "Fraction":
        gcd1 = gcd(self.num, self.den)
        self.num = int(self.num/gcd1)
        self.den = int(self.den/gcd1)