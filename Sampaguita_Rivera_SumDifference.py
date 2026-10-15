number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))


def calculate_sum():
    sum = number1 + number2
    print(f"Sum: {sum}")


def calculate_difference():
    difference = number1 - number2
    print(f"Difference: {difference}")

calculate_sum()
calculate_difference()