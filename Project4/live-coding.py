from typing import List

class Food:
    def __init__(self):
        pass

    def cost(self) -> int:
        raise NotImplementedError("Needs to be implemented in subclass")

class Atomic(Food):
    def __init__(self, price: int):
        self.price = price
        
    def cost(self):
        return self.price

class Composite(Food):
    def __init__(self, ingredients: List[Food]):
        self.ingredients = ingredients

    def cost(self) -> int:
        comp_cost = 0
        for ingredient in self.ingredients:
            comp_cost += ingredient.cost()
        return comp_cost

def main():
    garlic = Atomic(200)
    tomatoes = Atomic(100)
    sauce = Composite([garlic, tomatoes])

    parmesan = Atomic(100)
    mozzarella = Atomic(200)
    cheese = Composite([parmesan, mozzarella])

    yeast = Atomic(10)
    flour = Atomic(50)
    water = Atomic(0)
    salt = Atomic(5)
    crust = Composite([cheese, yeast, flour, water, salt])

    pepperoni = Atomic(500)
    toppings = Composite([pepperoni])

    pizza = Composite([crust, sauce, toppings])
    print(pizza.cost())


if __name__ == "__main__":
    main()