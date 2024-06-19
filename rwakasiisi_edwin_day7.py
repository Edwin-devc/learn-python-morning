#Inheritance and Polymorphism
"""
_summary_
Inheritance and method overriding
Polymorphism and method resolution
order
Abstract classes and interfaces

"""

# Inheritance and method overriding
"""summary_line
-- description
Inheritance and method overriding allows a class(child class) to inherit attributes and methods
from another class (parent class).

Key concepts
Base class (parent class): Class whose properties are inherited by another class
Derived classes (child class): Class that inherits attributes and properties from another base class

"""
# Example 1: Syntax create a class where a dog inherits from animal and overrides with a speak method
class Animal:
    def speak(self):
        return 'Mwe Mwe Mwe Mwe'

class Dog(Animal):
    def speak(self):
        return 'Barks'

animal = Animal()
dog = Dog()

print(animal.speak())
print(dog.speak())

# Polymorphism
# Polymorphism allows objects of different classes to be treated as objects of a common superclass
# Method resolution Order (MRO). is order in which python looks for a method in a hierarchy classes
#Example 2: How polymorphism works in python

class Animal:
    def speak(self):
        return 'Croooook'
    

class Dog(Animal):
    def speak(self):
        return 'Barks'
    
class Cat(Animal):
    def speak(self):
        return 'Meow'
    
def make_animal_speak(animal):
    print(animal.speak())

# dog = Dog()
# cat = Cat()

make_animal_speak(Dog())
make_animal_speak(Cat())


#Exercise 1: Create a simple application to manage different types of vehicles. Implement
#the derived class to demonstrate inheritance and polymorphism

"""
Requirements
1. Base class to Vehicle
Attributes: make, model and year
Methods: display_info()

2. Derived classes:
Car: inherit from vehicle
attributes: number_of_doors
Overrides: display_info()

Motorcycle: inherit from vehicle
Attributes: type_of_bike (cruiser, sport, touring)
Overrides: display_info()

#Exercise 2:
Create a function that accepts a list of vehicle objects and call their display_info() method
to print the details of each vehicle

"""

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def display_info(self):
        return f"Vehicle Info: {self.year} {self.make} {self.model}"
    
class Car(Vehicle):
    def __init__(self, make, model, year, number_of_doors):
        super().__init__(make, model, year)
        self.number_of_doors = number_of_doors
    def display_info(self):
        return f"Car Info: {self.year} {self.make} {self.model} {self.number_of_doors}"
    
class Motorcycle(Vehicle):
    def __init__(self, make, model, year, type_of_bike):
        super().__init__(make, model, year)
        self.type_of_bike = type_of_bike
    def display_info(self):
        return f"Motorcycle Info: {self.year} {self.make} {self.model} {self.type_of_bike}"
    
def display_vehicle_info(vehicles):
    for vehicle in vehicles:
        print(vehicle.display_info())

# Create a list of vehicles
vehicles = [
    Car("Toyota", "Camry", 2020, 4),
    Car("Honda", "Civic", 2021, 4),
    Motorcycle("Kawasaki", "Ninja", 2020, "Sport"),
    Motorcycle("Suzuki", "Gixxer", 2021, "Cruiser"),
]

# Call the display_vehicle_info function
display_vehicle_info(vehicles)
