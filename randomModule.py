import random


# chances = 0
# numbers = []

# while True:
#     range = int(input("Please enter any number: "))
#     chances += 1
#     if range == "q":
#         print("program ended")
#         break
#     elif range == "":
#         break

#     if chances > 10:
#         print("End!")
#         break
#     number = random.randint(1, range)

#     print(f"The random number is: {number}")


options = ["Rock", "Paper", "Scissor"]

# result = random.choice(options)
# print(result)

random.shuffle(options)

# Shuffule helps in shuffling the elements inside a List!
print(options)
