# A program that repeatedly prompts the user for a number until an invalid input is entered, then displays the average.

num_list = []

while True:
    try:
        num = float(input("Enter a number: "))
        num_list.append(num)
    except ValueError:
        break

if num_list:
    print("The average is:", sum(num_list) / len(num_list))
else:
    print("Invalid input.")