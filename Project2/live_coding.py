class Listener:
    def notify(self):
        raise NotImplementedError("Notify has not been implemented")

class Furniture(object):
    def __init__(self, material: str):
        self.material = material
        self.listeners = []

    def made_of(self) -> str:
        return f"This is made of {self.material}"

    def add_listeners(self, listener: Listener):
        self.listeners.append(listener)

    def notify_all(self):
        for idx, listener in enumerate(self.listeners):
            listener.notify()

    def use_it(self) -> str:
        raise NotImplementedError("The use it method was not defined for this subclass")

class Table(Furniture):
    def __init__(self, seats: int):
        super().__init__("Wood")
        self.seats = seats

    def use_it(self) -> str:
        self.notify_all()
        return f"Up to {self.seats} can sit here"

class Couch(Furniture):
    def __init__(self, cushions: int, material: str):
        super().__init__(material)
        self.cushions = cushions 

    def use_it(self) -> str:
        self.notify_all()
        return f"Sit on me ;)"

    def __str__(self) -> str:
        return f"A nice {self.material} couch with {self.cushions} cushions"

class WearListener(Listener):
    def __init__(self, condition: int, name: str):
        self.condition = condition
        self.name = name
    
    def notify(self):
        self.condition -= 1
        if self.condition < 1:
            print(f"{self.name} is worn out")

t1 = Table(8)
# print(t1.use_it())
# print(t1.made_of())
# print(t1.material)
# print(t1)

c1 = Couch(2, "Foam")
# print(c1)
# print(c1.use_it())

w1 = WearListener(2, "Jefferson")
t1.add_listeners(w1)
print(t1.use_it())
print(t1.use_it())