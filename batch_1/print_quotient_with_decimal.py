# Prompt user for two numbers and print the quotient rounded to two decimal places.
# If the second number is 0, print "Cannot divide by zero"

num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))

if num2 == 0:
    print("Cannot divide by zero.")
else:
    quotient = round(num1 / num2, 2)
    print("Quotient:", quotient)