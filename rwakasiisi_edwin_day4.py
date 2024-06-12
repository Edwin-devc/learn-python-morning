# Dictionaries
# Creating and using dictionaries
# Dictionary methods and operations

"""
Dictionaries in python are collections of key and values
-Unordered
-Mutable
-Indexed by keys

"""
# Example 1: Create a dictionary
# Create a dictionary for a student persuing software engineering,
# the key must be your name, age, technology interest, course and year of study.
# Put your own details

student_dict = {
    "name": "Edwin",
    "age": 23,
    "technology_interest": "Data Science",
    "course": "Software Engineering",
    "year": 'Year 3'
}

print(student_dict["name"])
# Access the value

# Modify the value
# Exercise 1: Modify age and technology

student_dict["age"] = 24
student_dict["technology_interest"] = "Machine Learning"
print(student_dict)

# Example 2: Adding keys and values
student_dict["email"] = 'erwakasiisi@gmail.com'
print(student_dict)

# Excercise2: Remove a key and a value
student_dict.pop("course")
print(student_dict)

# Example 3: Common Dictionary methods
"""
_summary_
get()       // returns the value for the specified key if the key is in the dictionary, if not it 
returns the default value
update()    //Updates the dictionary with the elements from another dictionary
pop()		//removes the specified key and return the corresponding value

"""
# Example 3: Use the get method to get the value
print(student_dict.get("technology_interest"))

# Exercise 3: Use the update method to update the value of age

student_dict.update({"age": 25})
print(student_dict)

# Exercise 4: Use if to check if the age key is present in the dictionary
if "age" in student_dict:
    print("The age key is present in the dictionary")
else:
    print("The age key is not present in the dictionary")

# Example 5:
#Keys(), values() and items() method

print(student_dict.keys())
print(student_dict.values())
print(student_dict.items())

"""
_summary_
keys()      returns a view of objects that displays a list of all keys
values()    returns a view of objects that displays a list of all values
items()     returns a view of objects that displays a list of dictionary keys and values tuple pairs

"""

# Exercise 5: Use the update method to change course and add a new
# key "WhatsApp_Number" to the dictionary

student_dict.update({"course": "BSSE", "WhatsApp_Number": "08123456789"})
print(student_dict)