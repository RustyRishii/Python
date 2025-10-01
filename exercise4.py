# Input exercise - Validate the user inputs
# 1. Username is not more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

# print(help(str))

username = input("Please enter your username: \n")

if len(username) < 12 and username.__contains__(" ") == False and username.isalpha() == False:
    print(f"Hello {username} welcome to the game")
