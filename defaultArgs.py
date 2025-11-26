# Default Arguments = A default value for certain parameters
#                     Default is used when the argument is omitted
#                     Make your functions more flexible, reduce # of arguments
#                     1. Positional 2. Default 3. Keyword 4. Arbitary


# def net_price(list_price, discount=0, tax=0.05):
#     return list_price * (1 - discount) * (1 + tax)


# final = net_price(500, 0, 0.05)
# print(final)


def hello(Greetings, title, name, city):
    print(f"{Greetings} {title} {name} from {city}")


hello(Greetings="Hello", city="London", name="Rishi", title="Mr")
