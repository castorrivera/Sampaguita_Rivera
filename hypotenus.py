import math



a = float(input("Enter the value of leg A: "))
b = float(input("Enter the value of leg B: "))

c1 = math.pow(a, 2) + math.pow(b, 2)

c2 = math.sqrt(c1)

print(f"the hypotenuse of {a} and {b} is {c2:.2f}.")