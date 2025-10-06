# Tuple = () ordered and unchangable. Duplicates OK. FASTER
# sourounded by normal brackets

fruits = (
    "Apple",
    "Banana",
    "Pear",
    "grapes",
    "Papaya",
    "Pineapple",
    "Guava",
    "dragonFruit",
    "Mango",
    "Mango",
)

# print(fruits)

# print(dir(fruits))
# print(len(fruits))


# print(fruits.count("Mango"))
# Count in tuple shows you the number of times the element has been repeated.
print(fruits.index("Mango"))
