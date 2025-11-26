class Cat:
    breed = input("What breed is your cat?")

    if breed != "Orange":
        print("Chaotic huh")
    else:
        print("Hmmm, that's peaceful")

    def __init__(self, breed, name, age):
        self.breed = breed
        self.name = name
        self.age = age
