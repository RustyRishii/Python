l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = [7, 8, 9]
l4 = ["*", 0, "#"]

keypad = [l1, l2, l3, l4]

for lines in keypad:
    for nums in lines:
        print(nums, end=" ")
    print()
