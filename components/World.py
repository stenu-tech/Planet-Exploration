import random
import string

from components.Planet import Planet

class World:
    def __init__(self):
        planets = self.create_planets()
        self.create_economy(planets)

    @staticmethod
    def factory(self):
        return random.randint(1,100)
    
    @staticmethod
    def generate_name():
        prefix = ''.join(random.choices(string.ascii_uppercase, k=1))  # Random uppercase letter
        suffix = ''.join(random.choices(string.digits, k=2))  # Two random digits
        separator = '-'  # Separator between prefix and suffix
        return prefix + separator + suffix

    def create_planets(self):
        planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
        self.planets = []

        for planet in planets:
            planet = Planet(planet, self.generate_name(), self.factory(self))
            print(planet.spaceship.name)
            print(planet.name)
            self.planets.append(planet)

        return planets
    

    def create_economy(self, planets):
        print("get more int - how")
