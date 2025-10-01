# Set = {} unordered and immutable but Add/Remove Ok. No Duplicates

# Unordered means that if you print print(fruits) all the elements inside the list will be printed randomly, not in the order you wrote.
# Represented with curly braces.


fruits = {
    "Apple",
    "Banana",
    "Pear",
    "grapes",
    "Papaya",
    "Pineapple",
    "Guava",
    "dragonFruit",
    "Mango",
}
# fruits.add("Watermelon")


# print(dir(fruits))

# print(f"The length of the fruit set is {len(fruits)}")
# print(fruits[0]) -> Indexing does not work in sets , so [0] or [1] does not work at all

fruits.add("Watermelon")
print(fruits)
