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

# Reading and Writing files in python
"""
1. Working with text files
2. Handling CSV files
3. JSON and XML file processing

"""

# Working with text files, open, read, write and close
# Note: Python  provides inbuilt functions to handle text files
# Key concepts
"""
-- description
Opening File: open() function
Reading File: read() function
Writing File: write() function
Close File: close() function

"""

# Example 3: Write a file and read a file
# Writing to a text file
with open('edwin.txt', 'w') as file:
    file.write('I am Edwin and I hate Python.\n')
    file.write('I use Python for data science.\n')
# Reading from a text file
with open('edwin.txt', 'r') as file:
	content = file.read()
	print(content)

# Handling CSV files
"""
CSV (Comma Seperated Values) file widely for data exchange.
Key Concepts:
Reading CSV files: Using 'csv.reader()'
Writing CSV: Using 'csv.writer
DictReader and DictWriter: The class read and write CSV files as dictionaries

"""
#Example 4: Writing and Reading CSV files
import csv

# Writing to a CSV file
with open('students.csv', 'w', newline='') as csv_file:
	writer = csv.writer(csv_file)
	writer.writerow(['name', 'position', 'course'])
	writer.writerow(['Edwin', 'student', 'BSE'])
	writer.writerow(['Arinda', 'student', 'BSE'])
	writer.writerow(['Alvin', 'student', 'CS'])

# Read from a CSV file
with open('students.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)

# JSON and XML file processing
"""summary_line
JSON (Javascript Object Notation ) and XML (eXtensible Markup Language) are formats used to
structure date

Key Concepts
Loading JSON Data: using json.load() for reading JSON file
Dumping JSON Data: using json.dump() for writing JSON file
Parsing JSON Data: Using json.loads() for handling JSON strings

"""

#Example 6: Write and read JSON file
import json

# writing to a JSON file

student_data = {
	'name': 'Edwin',
	'course': 'BSE',
	'year': 'Year 2'
}

# Open the file
with open ('student_data.json', 'w') as json_file:
	json.dump(student_data, json_file)

# Reading the JSON file
with open('student_data.json', 'r') as json_file:
	student_data = json.load(json_file)
	print(student_data)


# Exercise 2: Write and read the xml file.
import xml.etree.ElementTree as ET

# Write an XML file
# Create the root element
root = ET.Element("students")

# Create a student element
student = ET.SubElement(root, "student")
name = ET.SubElement(student, "name")
name.text = "Edwin"
course = ET.SubElement(student, "course")
course.text = "BSE"
year = ET.SubElement(student, "year")
year.text = "Year 2"

student = ET.SubElement(root, "student")
name = ET.SubElement(student, "name")
name.text = "Arinda"
course = ET.SubElement(student, "course")
course.text = "BSE"
year = ET.SubElement(student, "year")
year.text = "Year 2"

student = ET.SubElement(root, "student")
name = ET.SubElement(student, "name")
name.text = "Alvin"
course = ET.SubElement(student, "course")
course.text = "CS"
year = ET.SubElement(student, "year")
year.text = "Year 1"

# Convert the tree to a string and write it to a file
tree = ET.ElementTree(root)
with open('students.xml', "wb") as file:
    tree.write(file, encoding="utf-8", xml_declaration=True)

# reading from an XML file
# Parse the XML file
tree = ET.parse('students.xml')
root = tree.getroot()

# Iterate over the student elements and print them
for student in root:
    print(f"Name: {student.find('name').text}, Course: {student.find('course').text}, Year: {student.find('year').text}")

# Exercise 3: Using abstraction calculate the area and perimeter of a rectangle
class Shape:
    def __init__(self):
        pass

    def calculate_area(self):
        raise NotImplementedError

    def calculate_perimeter(self):
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

rectangle = Rectangle(5, 10)
print(f"Area: {rectangle.calculate_area()}")
print(f"Perimeter: {rectangle.calculate_perimeter()}")
