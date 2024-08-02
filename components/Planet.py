from components.Spaceship import Spaceship

class Planet:
        
    def __init__(self, name, spaceship, cargo):
            self.name       = name
            self.spaceship  = Spaceship(spaceship, 0, name)
            self.warehouse  = cargo