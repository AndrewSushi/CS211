from typing import List

class Animal(object):

    """Abstract base class for animals"""
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("{} makes sound {}".format(self.name, self._voice()))
    def _voice(self) -> str:
        """Returns the sound made by this kind of animal"""
        raise NotImplementedError("Subclass must provide _voice method")
# Implement Sheep and Dog to get the behavior shown below.

class Sheep(Animal):
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes sound Baaaa")

class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes sound Arf")

# marigold = Sheep("Marigold")
# charlie = Dog("Charlie")
# marigold.speak() # Expected output: "Marigold makes sound Baaaa"
# charlie.speak() # Expected output: "Charlie makes sound Arf"

class NumberGrid(object):
    """A square grid of number"""
    def __init__(self, values: List[List[int]]):
        self.values = values
        for row in values:
            assert len(row) == len(values) # Grid is a square

    def is_balanced(self) -> bool:
        row_sum = sum(self.values[0])
        for row in self.values:
            if row_sum != sum(row):
                return False

        col_sum = sum([row[0] for row in self.values])
        for col_i in range(len(self.values)):
            if col_sum != sum([row[col_i] for row in self.values]):
                return False
        return True

# assert NumberGrid([[2, 7, 6], [9, 5, 1], [4, 3, 8]]).is_balanced()
# assert not (NumberGrid([[2, 7, 6], [9, 7, 1], [4, 3, 8]]).is_balanced())
# print("Passed two simple test cases on 3x3 grid")

class Food(object):
    """Abstract base class for foods, basic or composite."""

    def calories(self) -> int:
        """Should return total calories"""
        raise NotImplementedError("Calories method not implemented")

class Basic(Food):
    """Not further decomposed into ingredients"""
    def __init__(self, name: str, calories: int):
        self.name = name
        self._calories = calories

    def calories(self) -> int:
        return self._calories

class Composite(Food):
    def __init__(self, name: str, ingredients: list):
        self.name = name
        self._ingredients = ingredients

    def calories(self) -> int:
        cals = 0
        for ingredient in self._ingredients:
            cals += ingredient.calories()
        return cals

# salt = Basic("salt", 0)
# crust = Composite("crust", [Basic("flour", 20), salt, Basic("yeast", 3)])
# tomatoes = Basic("tomatoes", 10)
# sauce = Composite("sauce", [tomatoes, Basic("garlic", 2), salt])
# cheese = Basic("mozzarella", 30)
# margherita = Composite("pizza margarita", [crust, sauce, cheese, tomatoes])
# print("{} calories in pizza margherita".format(margherita.calories()))
# # Expect:
# # 75 calories in pizza margherita

class Spillage(Exception):
    pass
class Bucket(object):
    """You can put stuff in! You can pour stuff out!"""
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        # Initially the bucket is empty
        self.holding = 0
    def pour_in(self, amount: int) -> None:
        """Pour amount of liquid into the bucket,
        if there is enough room left.
        """
        space = self.capacity - self.holding
        if amount > space:  
            raise Spillage("Too much! Overflowing!")
        self.holding += amount
    def pour_out(self, requested_amount: int) -> int:
        """Pour UP TO amount of liquid from the
        bucket. If more is requested than the bucket
        currently holds, pour out just what the bucket
        currently holds. Returns the amount of liquid
        actually poured out. See tests below for
        examples.
        """
        if requested_amount >= self.holding:
            holding = self.holding
            self.holding = 0
            return holding
        self.holding -= requested_amount
        return requested_amount


b = Bucket(20)
b.pour_in(10)
out = b.pour_out(7)
assert out == 7
out = b.pour_out(7)
assert out == 3
out = b.pour_out(7)
assert out == 0

class Point(object):
    """Point.x and Point.y are 'public' fields"""
    def __init__(self, x, y):
        self.listeners = [ ]
        self.x = x
        self.y = y
    def add_listener(self, listener: "PointListener") -> None:
        self.listeners.append(listener)
    def notify_all(self):
        for listener in self.listeners:
            listener.notify(self)
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.notify_all()

class PointListener(object):
    """ Complete me """
    def notify(self, point: Point):
        print(f"Point moved to {point.x},{point.y}")

# p = Point(5,5)
# p.add_listener(PointListener())
# p.move(4,3) # Expected output: "Point moved to 9,8"
# p.move(3,2) # Expected output: "Point moved to 12,10"

class Tree(object):
    """Abstract base class"""
    def max_leaf(self) -> int:
        raise NotImplementedError("max_leaf must be overridden")

class Leaf(Tree):
    """Leaves of tree hold positive integers"""
    def __init__(self, val: int) -> None:
        assert val > 0
        self.val = val
    def max_leaf(self) -> int:
        return self.val

class Interior(Tree):
    """Interior node has two subtrees"""
    def __init__(self, left: Tree, right: Tree) -> None:
        self.left = left
        self.right = right
    def max_leaf(self) -> int:
        return max(self.left.max_leaf(), self.right.max_leaf())

t = Interior(Leaf(4),Interior(Leaf(5),Leaf(3)))
assert t.max_leaf() == 5

