#Q1. Write a program that asks for your name and then greets you with your own name. Examples:
#If you enter your name as Viivi, the program will greet you with the wordsTerve, Viivi!
#If you enter your name as Ahmed, the program will greet you with the wordsTerve, Ahmed!
#Ans:
name = input("Enter your name: ")
print(f"Terve, {name}!")


#Q2. Write a program that asks for the radius of a circle and prints its area.
#Ans:
r = float(input("Enter a radius: "))
print(f"The area of the circle is {2 * 3.14 * r ** 2}")


#Q3. Write a program that asks for the base and height of a rectangle. The program prints the perimeter and area of
#the rectangle. The perimeter of a rectangle is the sum of the lengths of its four sides.
#Ans:
b = float(input("Enter a base: "))
h = float(input("Enter a height: "))
print(f"the perimeter of the rectangle is {2 * (b + h)} ")
print(f"the area of the rectangle is {b * h} ")


#Q4. Write a program that asks for three integers. The program prints the sum, product, and average of the numbers.
#Ans:
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
print(f"the sum of the number is {num1 + num2 + num3}")
print(f"the product of the number is {num1 * num2 * num3}")
print(f"the average of the number is {(num1 + num2 + num3) / 3}")


#Q5. Write a program that asks the user to enter a mass in medieval units: talents (leiviskä), pounds (naula), and lots (luoti). The program converts the input to full kilograms and grams and outputs the result to the user:
# One talent is 20 pounds.
# One pound is 32 lots.
# One lot is 13,3 grams.

mass1 = float(input("Enter a mass in talents: "))
mass2 = float(input("Enter a mass pounds: "))
mass3 = float(input("Enter a mass lots: "))
total_grams = (mass1 * 20 * 32 * 13.3) + (mass2 * 32 * 13.3) + (mass3 * 13.3)
kg = total_grams // 1000
gm = total_grams % 1000
print(f"the mass in modern system is {kg}kg and {gm}g")





