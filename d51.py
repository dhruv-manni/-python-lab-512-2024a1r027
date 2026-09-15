#write a python program to input two numbers and find their gratest common divisor using a loop
# Input two numbers from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Store original values for the final output display
a = abs(num1)
b = abs(num2)

# Use a loop to find the GCD using the Euclidean algorithm
while b != 0:
    remainder = a % b
    a = b
    b = remainder

# The GCD is now stored in 'a'
print(f"The Greatest Common Divisor (GCD) of {num1} and {num2} is: {a}")
