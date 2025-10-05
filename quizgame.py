answers = []
score = 0

while True:
    q1 = input("Which sport did lebron james play? \n a.BasketBall , b.FootBall \n")
    if q1.lower() == "q":
        print("Program ended")
        break
    elif q1.lower() == "a":
        score += 1
        answers.append(q1)

    q2 = input("Which sport did Virat kohli play? \n a. Cricket b. BaseBall")
    if q2 == "a":
        score += 1
        answers.append(q2)

    q3 = input("Which sport did Messi play? \n a. Cricket b. Football")
    if q3 == "b":
        score += 1
        answers.append(q3)
    break

print(answers)
print(score)
