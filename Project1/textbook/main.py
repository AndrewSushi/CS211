class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def move(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self) -> str:
        return f"{self.x}, {self.y}"

# x = Point(12, 4)
# print(x)
# y = Point(2, 10)
# print(y)
# x = x.move(y)
# print(x)
x = Point(3,5)
y = x
print(x.move(Point(4, 6)))
print(x, y)

# (5).str()
# __str__(5)
# [1, 2, 3].repr()

# print(str(5))
# print((5).__str__())
# print(repr([1, 2, 3]))
# print([1, 2, 3].__repr__())

class Wrap:
    def __init__(self, value: str):
        self.value = value

    def __str__(self) -> str:
        return f"{self.value}"

    def __repr__(self) -> str:
        return f"Wrap({self.value})"

# a = Wrap("alpha")
# b = Wrap("beta")
# print([a, b])
# print(a, b)

# x = [1, 2, 3]
# y = x
# y.append(4)
# print(x)
# print(y)