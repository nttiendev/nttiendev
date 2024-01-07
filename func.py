import random

# Generate two random numbers from 0 to 100
num1 = random.randint(0, 100)
num2 = random.randint(0, 100)

# Perform addition
sum = num1 + num2

# Perform subtraction
difference = num1 - num2

# Perform multiplication
product = num1 * num2

# Perform division
if num2 != 0:
    quotient = num1 / num2
else:
    quotient = "Cannot divide by zero"

# Print the results
print("First number: ", num1)
print("Second number: ", num2)
print("\n*********************************************\n")
print("Sum: ", sum)
print("Difference: ", difference)
print("Product: ", product)
print("Quotient: ", quotient)