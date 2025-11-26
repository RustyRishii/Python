list = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]


def binary_search(list, target):
    # i = list.index(target)
    j = list.index(target)
    for i in list.index(target):
        print(f"The index of the target is {j}")


binary_search(list, target=12)
