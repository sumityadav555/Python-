# Tuple
# It are immutable sequences used to store multiple values.

# Create tuple

# value = (1, 2)           # Normal tuple
# single_value = (1,)      # single tuple

# print(value)
# print(type(value))
# print(single_value)
# print(type(single_value))

# Acessing element 

num = (1, 2, 3)

# print(num[0])
# print(num[-1])

# Slicing

# print(num[1:])
# print(num[::-1])

# Unpacking

# a, b, c = (1, 2, 3)
# print(a)
# print(b)
# print(c)

# num = (1, 2, 3, 4)

# a,b,*c = num
# print(a)
# print(b)
# print(c)

# swap tuple
# a = 10
# b = 20

# Swapping without a temp variable
# a, b = b, a

# print(a)  # 20
# print(b)  # 10

# def get_coordinates():
#     return (42.0, -71.2)

# latitude, longitude = get_coordinates()

# print(latitude)   # 42.0
# print(longitude)  # -71.2

# Ignore two value

# person = ("Alice", 25, "Engineer", "New York")

# name, age, _, _ = person  # Ignoring last two values

# print(name)  # Alice
# print(age)   # 25

# The zip() function pairs elements from both lists, and tuple unpacking extracts them

# names = ["Alice", "Bob", "Charlie"]
# ages = [25, 22, 23]

# for name, age in zip(names, ages):
#     print(f"{name} is {age} years old")

# Basic Unpacking	           a, b = (10, 20)
# Extended Unpacking	       a, *b, c = (1,2,3,4,5)
# Swapping Variables	       a, b = b, a
# Function Returns	       x, y = get_values()
# Loop Unpacking	           for k, v in dict.items():
# Nested Unpacking	       name, (age, job) = data
# Ignoring Values	           name, _, _ = person

tup = (1, 2, 3, 2, 2)
print(tup.count(2))  # 3 (counts occurrences of 2)
print(tup.index(3))  # 2 (index of first occurrence)

