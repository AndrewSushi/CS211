from typing import Tuple
from math import sqrt

class Point:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y

    def move(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
    
    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"

    def dist(self, other: "Point"):
        """Euclidean distance = sqrt(dx^2 + dy^2)"""
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx * dx + dy * dy)

class Shape:
    """An abstract Base Class"""
    def __init__(self):
        raise NotImplementedError("Do not instantiate 'Shape'; it is abstract")

    def area(self) -> int:
        raise NotImplementedError(f"Class {self.__class__} didn't define 'Area'")

    def translate(self, delta:Point) -> "Shape":
        raise NotImplementedError(f"Class {self.__class__} didn't define 'Translate'")

class Rect(Shape):
    def __init__(self, min_vals:Point, max_vals:Point):
        self.min_pt = min_vals
        self.max_pt = max_vals

    def area(self) -> int:
        height = self.max_pt.y - self.min_pt.y
        width = self.max_pt.x - self.min_pt.x
        return height * width

    def translate(self, delta: Point) -> "Rect":
        return Rect(self.min_pt.move(delta), self.max_pt.move(delta))

    def __str__(self) -> str:
        return f"Rect({self.min_pt}, {self.max_pt})"

    def __repr__(self) -> str:
        return f"Rect({self.min_pt}, {self.max_pt})"

class Square(Rect):
    def __init__(self, anchor: Point, size: int):
        self.min_pt = anchor
        self.max_pt = self.min_pt.move(Point(size, size))
        self.size = size

    def __str__(self) -> str:
        return f"Square({self.min_pt}, {self.size})"

    def side(self) -> int:
        return self.size

    def translate(self, delta: Point) -> "Square":
        return Square(self.min_pt.move(delta), self.size)

def normal_intersect(p1_x, p1_y, p2_x, p2_y, px, py) -> Tuple:
    if p2_x == p1_x:
        return p1_x, py
    elif p2_y == p1_y:
        return px, p1_y

    seg_slope = (p2_y - p1_y) / (p2_x - p1_x)
    normal_slope = 0 - (1.0 / seg_slope)

    # For y=mx+b form, we need to solve for b (y intercept)
    seg_b = p1_y - seg_slope * p1_x
    normal_b = py - normal_slope * px

    # Combining and subtracting the two line equations to solve for intersect
    x_intersect = (seg_b - normal_b) / (normal_slope - seg_slope)
    y_intersect = seg_slope * x_intersect + seg_b
    # Colinear points are ok!

    return (x_intersect, y_intersect)

class Triangle(Shape):
    def __init__(self, p1: Point, p2: Point, p3: Point):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def translate(self, delta: Point) -> "Triangle":
        return Triangle(self.p1.move(delta), self.p2.move(delta), self.p3.move(delta))

    def __str__(self) -> str:
        return f"Triangle({self.p1}, {self.p2}, {self.p3})"

    def __repr__(self) -> str:
        return f"Triangle({repr(self.p1)}, {repr(self.p2)}, {repr(self.p3)})"

    def area(self) -> float:
        ix, iy = normal_intersect(self.p2.x, self.p2.y, self.p3.x, self.p3.x, self.p1.x, self.p1.y)

        intercept = Point(ix, iy)
        base = self.p2.dist(self.p3)
        height = self.p1.dist(intercept)
        return 0.5 * height * base


# p1 = Point(13, 5)
# print(type(p1))
# print(p1)
# print(p1.__repr__())
# p2 = Point(4, 8)
# print(type(p2))
# print(p2)
# print(p2.__repr__())
# p3 = Point(3, 10)
# print(type(p3))
# print(p3)
# print(p3.__repr__())

# p1 = Point(3,5)
# p2 = Point(8,8)
# r1 = Rect(p1, p2)
# p3 = Point(6, 5)
# r2 = r1.translate(p3)  # Treat Point(4,5) as (dx, dy)
# print(f"{r1} + {p3} => {r2}")
# print(f"Area of {r1} is {r1.area()}")

# p1 = Point(3, 5)
# sq = Square(p1, 5)
# print(sq)

# p1 = Point(3, 5)
# sq = Square(p1, 5)
# print(sq)
# s2 = sq.translate(Point(2,2))
# print(s2)
# print(sq.side())
# print(s2.side())

def darn_close(n, m, sigma: int = 3):
    """Within 10^(-sigma), default is
    sigma=3 or 1/1000
    """
    fudge = 1.0
    for precision in range(sigma):
        fudge = fudge / 10.0
    return abs(n - m) <= fudge


def triangle_tests():
    """Better test with triangles in different orientations,
    but we need triangles for which it is easy to calculate
    expected area by other means.
    """
    # A simple right triangle --- easy to calculate
    rt = Triangle(Point(0, 0), Point(0, 1), Point(2, 0))
    assert darn_close(rt.area(), 1.0), "Right triangle size should be 1"

    # Should be the same if I reorder the points
    rt = Triangle(Point(0, 1), Point(0, 0), Point(2, 0))
    assert darn_close(rt.area(), 1.0), "Right triangle size should still be 1"

    # Should be the same if I rotate it 45 degrees
    rt = Triangle(Point(sqrt(2.0), sqrt(2.0)), Point(0, 0),
                  Point(1.0 / sqrt(2.0), -1.0 / sqrt(2.0)))
    assert darn_close(rt.area(), 1.0), "Rotated size should still be 1"

    # And again if I nudge it off (0,0)
    rt = rt.translate(Point(3.0, 3.0))
    assert darn_close(rt.area(), 1.0), "Nudged and rotated should still be 1"
    print("Triangle tests passed")

def smoke_test():
    print("=== Smoke test ===")
    # Basic tests for Rect
    p1 = Point(3, 5)
    p2 = Point(8, 7)
    r1 = Rect(p1, p2)
    mvmt = Point(4, 5)
    r2 = r1.translate(mvmt)  # Treat Point(4,5) as (dx, dy)
    print(f"{r1} + {mvmt} => {r2}")
    print(f"Area of {r1} is {r1.area()}")
    # ShapeList is a list of Shape objects
    # li = ShapeList()
    # li.append(Rect(Point(3, 3), Point(5, 7)))  # 2x4 = 8
    # li.append(Square(Point(2, 2), 2))  # 2x2 = 4
    # li.append(Triangle(Point(0, 0), Point(0, 1), Point(2, 0)))  # Area 1
    # print(f"ShapeList {li}")
    # print(f"Combined area is {li.area()}, expecting 13")
    # Basic tests for Square
    print("Squares are Rects")
    p1 = Point(3, 5)
    sq = Square(p1, 5)
    print(f"Square from {p1} side {sq.side()}, {repr(sq)} prints as {sq}")
    s2 = sq.translate(Point(2, 2))
    print(f"{sq} nudged (2,2) is {s2}")
    print("Triangle area tests")
    triangle_tests()



if __name__ == "__main__":
    smoke_test()
