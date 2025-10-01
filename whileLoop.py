# # While loop = execute some code WHILE some condition remains True

# # name = input("Enter your name: \n")

# # while name == "":
# #     print("You did not enter the name")
# #     name = input("Enter your name: \n")

# # print(f"hello {name}")


# # age = int(input("Enter your age: \n"))

# # while age < 0:
# #     print("Age cannot be negative")
# #     age = int(input("Enter your age: \n"))


# # print(f"You are {age} years old")

# food = input("Enter a food you like: ")

# while not food == "q":
#     print(f"You like {food}")
#     food = input("Enter a food you like: ")
# print("Bye")

# Countdown Timer:-
# count = int(input("Please enter a numner"))
# while count > 0:
#     print(f"{count}")
#     count -= 1  # Increment count to eventually make the condition False
# print("Loop finished!")


# Sum of natural numbers

n = int(input("Please enter a number: \n"))
sum = 0

while n > 0:
    print(f"the sum is{sum}")
    sum += n
print("Loop finished")
