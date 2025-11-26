# Default arguments in python
import time


# While passing arguments in functions, an argument with default will come only & only in the end.
# Like in this case, start has 0 default value and it only comes in the end.


def count(end, start=0):
    for i in range(start, end + 1):
        print(i)
        time.sleep(1)
    print("Done")


count(30, 15)
