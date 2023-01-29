"""Create a Class
Create a constructotr
Must have one built in 
Must have one custom method
"""

class Food:
    def __init__(self, kind:str, ammount:int):
        self.kind = kind
        self.amount = ammount

    def __str__(self) -> str:
        return f"There are {self.amount} {self.kind}!"

    def eat(self):
        if self.amount <= 0:
            print("There is no food to be eaten")
        self.amount -= 1
        print("MMMM. Food")

pizza = Food("Pizza", 1)
pizza.eat()
pizza.eat()
pizza.eat()
pizza.eat()
pizza.eat()