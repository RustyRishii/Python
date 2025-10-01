fruits = [
    "Apple",
    "Banana",
    "Watermelon",
]

veggies = [
    "Capsicum",
    "Carrot",
    "Cucumber",
]

meat = ["Chicken", "Beef", "Bacon"]

groceries = [fruits, veggies, meat]

# print(groceries)

# print(groceries[0][0], groceries[1][1], groceries[2][2])
# print(dir(groceries))

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()
