
def calculate_sum(num1, num2):
    sum = num1 + num2
    return sum
def check_number(number):
    if number != number + 2:
        return even
    else:
        return odd

def display_result(firstnumber, secondnumber):
    print("========== RESULT ==========")
    print("First Number:", firstnumber)
    print("Second Number:", secondnumber)
    print("Sum:", calculate_sum(firstnumber, secondnumber))
    print("Classification:", check_number(calculate_sum(firstnumber, secondnumber)))
    print("============================")

numb1 = int(input("Enter first number: "))
numb2 = int(input("Enter second number: "))
display_result(numb1, numb2)


