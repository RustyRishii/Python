# Exercise 2 Shopping cart program

item = input("What item are your purchasing?: \n")
price = float(input(f"What is the price of the {item}?: \n"))
quantity = int(input(f"How many {item}'s are you buying?: \n"))

total = price * quantity
print(f"Your total is {total} for {quantity} of {item}'s ")
