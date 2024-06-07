""""
Control Structures
Conditional statements (if, elif, else)
Loops (for, while)
omprehensions (list, dictionary comprehensions)

"""

age = 23

if age > 18:
    print("You are an adult")
elif age > 65:
    print("You are a senior citizen")
else:
    print("You are a youth")

grade = 56
if grade >= 90:
    print('Excellent')
elif grade >= 80:
    print("Very good")
elif grade >= 70:
    print("Good")
else:
    print('Not good')

"""
_summary_
	Exercise: Scenario: Write a python script to determine the price
of a movie based on age. Condition children under 13 get discount for price
=shs 1000
Teenagers between 13 and get discount for price = shs 500
Adults 18 and above pay full price = shs 2000
Otherwise, senior citizens
"""

full_price = 2000
age = int(input("Enter your age: "))

#check if age is between 13 and 18
if age < 13:
    price = full_price - 1000
    print(price)
elif age >= 13 and age <= 18:
    price = full_price - 500
    print(price)
elif age > 18 and age <= 65:
    print(full_price)
else:
    price = 5000
    print(price)

"""
_summary_
for loop iterates over a sequence (list, tuple, dictionary, set, string)
The while loop repeats as long as a condition is true
"""
cars = ['Audi', 'BMW', 'Mercedes', 'Volkswagen', 'Ferrari']
for car in cars:
    print(car)


""""
_summary_
	1. Create your own list of favorite colors using for loop
	2. Create a reverse of the input 12345 to be 54321 using while loop
"""

favourite_colors = []
# getting input
for number in range(5):
    color = input("Enter your favourite color: ")
    favourite_colors.append(color)

print(favourite_colors)
print("\n")

# reversing list
# using the for loop
reversed_favorite_colors = favourite_colors[::-1]
for color in reversed_favorite_colors:
    print(color)
print("\n")

# using the while loop
count = 0
while count < len(favourite_colors):
    print(favourite_colors[count])
    count += 1

# using the list
print(favourite_colors)
