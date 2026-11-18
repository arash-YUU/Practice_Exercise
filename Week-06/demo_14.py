# Programmer: Arash
# Date: 11-17-2026
# Purpose: Compare two numbers
# Instructor: Deodat Sharma

def compare_numbers(num1, num2):
    if num1 > num2:
        print(f"{num1} is greater than {num2}")
    elif num2 > num1:
        print(f"{num2} is greater than {num1}")
    else:
        print("The numbers are equal")


number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

compare_numbers(number1, number2)