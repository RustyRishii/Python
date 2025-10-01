# Temeperature conversions

unit = input("f or c: \n")
temp = float(input("Please enter the temeprature: \n"))

if unit == "f":
    fTemp = (temp - 32) * 5/9
    print(f"{temp} in Farenheit is {fTemp}F")
elif unit == "c":
    cTemp = (temp * 9/5) + 32
    print(f"{temp} in celcius is {cTemp}c")
else:
    print("Pleae enter a f or c")
