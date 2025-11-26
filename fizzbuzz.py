num1 = int(input("Please enter the range for fizzbuzz game: "))
times = 0
for i in range(1, num1):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i} FizzBuzz")
        times += 1
        print(times)
    elif i % 3 == 0:
        print(f"{i} Fizz")
    elif i % 5 == 0:
        print(f"{i} Buzz")
    else:
        print(i)
print(f"FizzBuzz happens {times} times b/w 0 and {num1}")
