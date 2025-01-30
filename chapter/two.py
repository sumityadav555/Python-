# control flow and loop
# Write a Python program to check if a number is even or odd.

# num = int(input("Enter a number: "))

# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# Print the Fibonacci series up to n terms.

term = int(input("Enter no of term : "))

pre = 0
next = 1

if term == 1:
    print(0)
else:
    while term:
        result = pre
        pre = next 
        next = pre + result
        print(result, end = ' ')

        term -= 1

print("\nThe sequence")




