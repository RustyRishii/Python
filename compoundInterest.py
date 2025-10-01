#  Compound interest calculator.

rate = float(input("Please enter the rate"))
time = float(input("Please enter the time "))
principle = float(input("Please enter the pricncple amount"))

while rate <= 0:
    print("Rate can't less 0 or less")
    rate = int(input("Please enter the rate"))

while time <= 0:
    print("Time can't 0 or less")
    time = float(input("Please enter the time "))

while principle <= 0:
    print("Principle can't be 0 or less")
    principle = float(input("Please enter the pricncple amount"))


compound = principle * pow((1+rate/100), time)
print(compound)
