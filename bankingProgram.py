deposit = input("Do you what to deposit money in the bank? Yes/No")


while deposit.lower() == "yes":
    print("welcome to the bank, How much would you like to deposit?")
    amount = float(input())
    if amount < 0:
        print("Apologies, that is not possible, The ")
    elif amount > 0:
        print("Your money has been deposited into your accont.")

    # Ask if they want to deposit again
    deposit = input("Do you want to deposit more money? Yes/No")
