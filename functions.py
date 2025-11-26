# Function:- A block of resuable code
#            place () after the function name to invoke it.

# name = input("Please enter your name: ")


# def myFunction(name):
#     print(f"hello {name}")


# myFunction(name)

# num1 = int(input("Please enter the first number: "))
# num2 = int(input("Please enter the second number: "))


# def Addition(num1, num2):
#     result = num1 + num2
#     print(f"The addition is {result}")


# def Substraction(num1, num2):
#     result = num1 - num2
#     print(f"The substraction is {result}")


# def Multiplication(num1, num2):
#     result = num1 * num2
#     print(f"The Multiplication is {result}")


# def Division(num1, num2):
#     result = num1 / num2
#     print(f"The division is {result}")


# Addition(num1, num2)
# Substraction(num1, num2)
# Multiplication(num1, num2)
# Division(num1, num2)


fname = input("What is your first name?")
lname = input("What is your last name?")


def nameFunc(fname, lname):  # Here fname & lname are paramters
    return f"So your name is {fname} {lname}"


name = nameFunc(fname, lname)  # Here fname & lname are Arguments
print(name)


# def create_name(first, last):
#     first = first.capitalize()
#     last = last.capitalize()
#     return first + " " + last


# name = create_name("Bro", "code")
# print(name)
