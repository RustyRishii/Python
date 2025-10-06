import random

chances = 0
number = random.randint(1, 10)

while True:
    guess = int(input("Guess the number: "))

    if guess > number:
        chances += 1
        print("Less than your guess")
    elif guess < number:
        chances += 1
        print("Greater than your guess")
    # elif guess > 10:
    #     chances += 1
    #     print(chances)
    #     print("Out of range")
    #     break
    elif guess == number:
        chances += 1
        print("correct")
        print(f"Total chances for the guess: {chances}")
        break
