#  function

# Write a function to find the factorial of a number.
# def factorialOfNumber(num):  # parameter
#     result = 1

#     for i in range(1,num+1):
#         result *= i

#     return result

# num = int(input("Input value: "))

# factorial = factorialOfNumber(num)  # function call by passing argument
# print(f"Factorial of {num} is: {factorial}")


# Implement a function to check if a string is a palindrome.
# A string which read same from backward or forward is called palindrome

def isPlaindrome(string):
    rev_string = ''
    for i in string:
        rev_string = i + rev_string

    if string == rev_string:
        return True
    else:
        return False

user_input = input("Enter a string: ")

if isPlaindrome(user_input):
    print("Plaindrome")
else:
    print("It is not plaindrome")


