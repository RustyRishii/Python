import random

game = ("Rock", "Paper", "Scissor")
chance = 0

while True:
    H1 = input("Choose b/w, Rock, paper & Scissor")

    if H1 == "q":
        print("Broken")
        break

    C1 = random.choice(game)
    print(C1)
    if H1 == "Paper" & C1 == "Rock":
        print("Human wins")

    H2 = input("Choose b/w, Rock, paper & Scissor")
    C2 = random.choice(game)

    if H2 == "Scissor" & C2 == "Paper":
        print("Human wins")

    H3 = input("Choose b/w, Rock, paper & Scissor")
    C3 = random.choice(game)

    if H3 == "Rock" & C3 == "Scissor":
        print("Computer wins")
