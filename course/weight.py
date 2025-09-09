# The weights exercise.
# import math

weight = float(input("Please enter your weight: \n"))
unit = input("kg or lb?")

if unit == "lb":
    kgResult = weight * 0.45359237
    print(f"Your weight in lb is {kgResult}")
elif unit == "kg":
    lbResult = weight * 2.20462
    print(f"Your weight in kg is {round(lbResult, 1)}")
else:
    print("Please enter either kg or lb")
