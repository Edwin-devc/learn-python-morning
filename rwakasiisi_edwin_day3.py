# Comprehensions (list, dictionary comprehensions)

# Python operators
"""
_summary_

Name of the operator	Symbol with Example
Addition			        x + y
Subtraction			        x - y
Multiplication			    x * y
Division			        x / y
Modulus				        x % y
Exponentiation			    x ** y
Floor division			    x // y

# Example of Comparison operators

Name of the operator	Symbol with Example
Equal				        x = y
Not equal			        x != y
Greater than			    x > y
Less than			    x < y
Greater than or equal to	x >= y
Less than or equal to		x <= y	

# Example of Logical operators

Name of the operator	Symbol with Example
and				            and
or				            or
not				            not

# Example of Membership operators

Name of the operator	Symbol with Example
in				            x in y
not in				        x not in y

# Example of Python Bitwise operators

Name of the operator	Symbol with Example
AND				            &
OR				            |
XOR				            ^
NOT				            ~

# Python cases
1. snake_case
2. camelCase
3. PascalCase
4. UPPERCASE
5. kebab-case

"""

# Comprehensions (list, dictionary comprehensions)
"""
_summary_
Comprehensions provide a concise way to create lists and dictionaries
What is the symbol for
lists		    [] square brackets //used to store multiple items in a single variable
dictionaries	{} curly brackets  //used to store values in key:value pairs
"""
# Example 1: Basic List Comprehensions
# create a list of squares in range of 10
list_of_squares = [x**2 for x in range(10)]
print(list_of_squares)

# Exercise1: Create a list of even squares in the range of 20
even_squares = [x**2 for x in range(20) if x % 2 == 0]
print(even_squares)

# Example 2: Dictionary Comprehensions
# Create a dictionary comprehension for favorite cars count the length of the characters
favorite_cars = ['BMW', 'Jeep', 'Mercedes', 'fordraptor']
car_lengths = {car: len(car) for car in favorite_cars}
print(car_lengths)

# Exercise 2: Create a list of tuple where each tuple contains a number and its cube for numbers
# between 1 and 10 using a dictionary comprehension

cube_numbers = {x: (x,x**3) for x in range(1, 11)}
print(cube_numbers)