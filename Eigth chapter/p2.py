def convert(temp):
    fahrenheit = temp * (9/5) + 32
    return fahrenheit

celsius = float(input("Enter the temperature: "))
print(f"The given temp {celsius} is equal to {convert(celsius)}")