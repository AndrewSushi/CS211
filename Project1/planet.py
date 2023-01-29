import math

class Planet:
    def __init__(self, name, radius, mass, distance):
        self.__name = name
        self.__radius = radius
        self.__mass = mass
        self.__distance = distance

    def get_name(self):
        return self.__name

    def get_radius(self):
        return self.__radius

    def get_mass(self):
        return self.__mass

    def get_distance(self):
        return self.__distance

    def get_volume(self):
        v = 4 / 3 * math.pi * self.__distance ** 3
        return v

    def get_surface_area(self):
        sa = 4 * math.pi * self.__radius ** 2
        return sa

    def get_density(self):
        d = self.__mass / self.get_volume()
        return d
    
myPlanet = Planet("X25", 45, 198, 1000)

print(myPlanet.get_name())
print(myPlanet.get_radius())
print(myPlanet.get_mass())
print(myPlanet.get_distance())
print(myPlanet.get_volume())
print(myPlanet.get_surface_area())
print(myPlanet.get_density())