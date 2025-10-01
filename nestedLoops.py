rows = int(input("Please enter the number of rows: "))
cols = int(input("Please enter the number of cols: "))


for x in range(rows):
    for y in range(1, cols):
        print(y, sep=", ", end=" ")
    print()
