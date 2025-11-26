import math

operator = input("Which operation would you like to make ?( + - * /): \n")

num1 = float(input("Please enter the num1: \n"))
num2 = float(input("Please enter the num2: \n"))

if operator == "+":
    resultAdd = num1 + num2
    print(round(resultAdd, 3))
elif operator == "-":
    subResult = num1 - num2
    print(subResult)
elif operator == "*":
    productResult = num1 * num2
    print(productResult)
elif operator == "/":
    divResult = num1 / num2
    print(divResult)
else:
    print(f" {operator} is invalid. Please Enter something from the above please")
