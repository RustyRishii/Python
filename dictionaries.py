# Dictionary: a collection of {key: value} pairs
#              ordered & changable. No Duplicates

# In this case, "Countries" is the key and their "Capitals" are values. Both combined are called key value pair


capitals = {
    # Key: #Value -> Pair
    "USA": "Washington DC",
    "India": "Delhi",
    "Croatia": "Zagreb",
    "UK": "london",
}

print(dir(capitals))
# popped_value = capitals.pop("USA")
# print(popped_value)

print()
print()


# Returns only the values of the keys,
# In this case, it will only prints the values(capitals), not the keys(counties)
print(capitals)
print(capitals.keys())
print(capitals.values())
print()
print()


# print(capitals.values())

print()
print()

# This gets the value of the specifi key in the dictionary. here it will print Not found, if the key is not available.
# print(capitals.get("UK", "Not found"))

print()
print()


# this removed the last key value pair of the dictionaty.
# capitals.popitem()
# print(capitals)

# country = input("Enter country name")
# if capitals.get(country):
#     print("This value exists")
# else:
#     print("This value doesn't exist")

# capitals.update({"Germany": "Berline"})
# print(capitals)
# capitals.update({"USA": "Detroit"})
# print(capitals)


default = capitals.setdefault("India", "Delhi")
print(default)


print()
copycat = capitals.copy()
print(copycat)

print()
print()

# Wraps all the key value pairs in the a tuple () tuple is brackets
items = capitals.items()
print(items)
