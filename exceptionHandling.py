# exception:- An event that interrupts the flow of the program.
#             (Zero division error, TypeError, ValueError)
#             1.Try 2.Catch 3.Finally


try:
    number = int(input("Enter a number"))
    print(1 / number)
except ZeroDivisionError:
    print("You can't divide it by Zero, you idiot")
except TypeError:
    print("Enter only numbers please")
except ValueError:
    print("Please enter a valid number.")
finally:
    print("Hahahhah")
