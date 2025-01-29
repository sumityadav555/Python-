# List 
# Lists are mutable sequences used to store multiple items.
# creating list

# my_list = [1, 2, 3, 4]  # Normal list
# single_list = [1]       # Single list

# print(my_list)
# print(single_list)

# check datatype

# print(type(my_list))
# print(type(single_list))

# Slicing list

my_list = ["Apple", "Banana", "Mango", "Litchi"]

print(my_list[1:4])
print(my_list[:4])
print(my_list[:])
print(my_list[::-1])

# list method

num = [1,2,3]

num.append(4)           # add element at the end of the list
num.insert(2, 3)        # insert element at the given index 
num.extend([4,5,6])     # merged parameter as list to extend the existing list
num.remove(4)           # It remove give element from the list
num.pop()               # It remove the last element of list
num.reverse()           # it reverse the list
num.sort()              # It arrange the element into asecending or descending order
print(num)
