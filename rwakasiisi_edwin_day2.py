# """"

# """

# # age = 23

# # if age > 18:
# #     print("You are an adult")
# # elif age > 65:
# #     print("You are a senior citizen")
# # else:
# #     print("You are a youth")

# full_price = 2000
# age = int(input("Enter your age: "))


# #check if age is between 13 and 18
# if age < 13:
#     price = full_price - 1000
#     print(price)
# elif age >= 13 and age <= 18:
#     price = full_price - 500
#     print(price)
# elif age > 18 and age <= 65:
#     print(full_price)
# else:
#     price = 5000
#     print(price)


# favourite_colors = []

# for number in range(5):
#     color = input("Enter your favourite color: ")
#     favourite_colors.append(color)

# print(favourite_colors)


favourite_colors2 = []
count = 5
while count > 0:
    color_reverse = input(f"Enter your favourite color {count}: ")
    favourite_colors2.append(color_reverse)
    count -= count

print(favourite_colors2)

