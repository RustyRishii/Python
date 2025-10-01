# Logical operators - evaluate multiple conditions(or, and, not)
#                      or = atleast one condition must be True
#                      and = both conditions must be True
#                      not = inverts the condition(
#                            if it's false it'll become true.
#                            if it's true, it'll become false


temp = int(input("What is the temeprature?: \n"))
is_raining = True

# if temp > 35 or temp < 20 or is_raining:
#     print("The outdoor event is cancelled")
# else:
#     print("The outdoor event is still scheduled")


# if temp <= 20 and is_raining:
#     print("Oh, it's raining. Cancel the plan")
# else:
#     print("it's raining")

if not temp >= 10:
    print("Hello")
