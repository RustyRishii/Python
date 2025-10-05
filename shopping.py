# Exercise:- Shopping cart

foods = []
prices = []
total = 0

while True:
    food = input("Please enter the food items (q to quit): ")
    if food.lower() == "q":
        print("Program ended")
        break
    else:
        price = float(input(f"Enter the price of {food}: $ "))
        foods.append(food)
        prices.append(price)

print("---------Cart--------")

print()

for food in foods:
    print(food, end=" ")

for price in prices:
    total += price

print(f"Your total is ${total} ")
