#Imported the math module so we can use math formulas in python
import math

#Input the coordinates so that the distance can be calculated
x1 = float(input("enter number for x¹ "))
print("number entered")
y1 = float(input("enter number for y¹ "))
print("number entered")
x2 = float(input("enter number for x² "))
print("number entered")
y2 = float(input("enter number for y² "))
print("number entered")

x3 = x2 - x1
y3 = y2 - y1
#giving the answers to the power of 2
answer1 = math.pow(x3, 2)
answer2 = math.pow(y3, 2)

#Adding both answers together
subfinal = answer1 + answer2

final = math.sqrt(subfinal)

print(f"the distance is: {final:.2f}")

#1. The math library helped me simplify my program because it allowed me to use math.sqrt and math.pow to help me skip having to make long lines of code just to calculate a number to a power and square root.

#2. The library made it easier to do square roots and calculating powers rather than doing it from scratch.

#3. The program would be much harder without sqrt() and pow() because I would have to get the roots and calculate powers using only the base python set of operations like additon, subrtraction, multiplication, and division.
