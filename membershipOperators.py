# Operators:- used to test whether a value or variable is found in the sequence
#             (String, List, Tuple, Set or dictionary)
#             1. in
#             1. not in


# word = input("Please enter the word: ")
# letter = input("Please enter the guess: ")

# if letter in word:
#     print(f"There is {letter} in {word} at {word.index(letter)}")
# else:
#     print(f"{letter} was not found")


students = {"Spongebob", "Rick", "Morty"}

name = input("Enter the student name pls: ")

if name in students:
    print(f"Yes {name} is found.")
else:
    print(f"No, {name} is not found")
