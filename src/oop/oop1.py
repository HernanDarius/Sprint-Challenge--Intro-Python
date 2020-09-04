# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

#Vehicle is the base class, as it defines the qualities of a Vehicle.
class Vehicle:
    def __init__(self, name, moves):
        self.name = name
        self.moves = moves
    
    def __str__(self):
        return f"This is a {self.name}.\n Does it move? {self.moves}"

class GroundVehicle(Vehicle):
    def __init__(self, name, moves, how):
        super().__init__(name, moves)

        self.how = how
    
    def __str__(self):
        return f"""This is a {self.name}.\n Does it move? {self.moves}\n 
                   How does it move? {self.how}"""

class FlightVehicle(Vehicle):
    def __init__(self, name, moves, how):
        super().__init__(name, moves)

        self.how = how
    
    def __str__(self):
        return f"""This is a {self.name}.\n Does it move? {self.moves}\n 
                   How does it move? {self.how}"""

class Car(GroundVehicle):
    def __init__(self, name, moves, how, wheel_num):
        super().__init__(name, moves, how)

        self.wheel_num = wheel_num
    
    def __str__(self):
        return f"""This is a {self.name}.\n Does it move? {self.moves}\n 
                   How does it move? {self.how}\n How many wheels?{self.wheel_num}"""
    
class Motorcycle(GroundVehicle):
    def __init__(self, name, moves, how, wheel_num):
        super().__init__(name, moves, how)

        self.wheel_num = wheel_num
    
    def __str__(self):
        return f"""This is a {self.name}.\n Does it move? {self.moves}\n 
                   How does it move? {self.how}\n How many wheels?{self.wheel_num}"""

class Airplane(FlightVehicle):
    def __init__(self, name, moves, how, environment):
        super().__init__(name, moves, how)

        self.environment = environment
    
    def __str__(self):
        return f"""This is a {self.name}.\n Does it move? {self.moves}\n 
                   How does it move? {self.how}\n Where?{self.environment}"""

class Starship(FlightVehicle):
    def __init__(self, name, moves, how, environment):
        super().__init__(name, moves, how)

        self.environment = environment
    
    def __str__(self):
        return f"""This is a {self.name}.\n Does it move? {self.moves}\n 
                   How does it move? {self.how}\n Where?{self.environment}"""
