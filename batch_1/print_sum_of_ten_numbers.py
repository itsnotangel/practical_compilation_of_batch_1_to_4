# Prompt the user to enter ten numbers and print the sum of the numbers.

sum_total = 0

for count in range(10):
    number = float(input("Enter number " + str(count + 1) + ": ")) 
    sum_total += number

print("Sum of ten numbers:", sum_total) 