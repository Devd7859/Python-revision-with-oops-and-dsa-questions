#Question 1: Menu with Options
import math
def Menu():
    print("Choose what do you want to do: ")
    print("1: Find A square root of a number")
    print("2: Find Area or perimeter of Triangle and Circle: ")
    print("3: Solve Quadratic Equation: ")
    print("4: Swap Two Numbers: ")
    print("5: Kilometers to Miles: " )
    print("6: Celsius to Fahrenheit: ")
    print("7: to exit the program:")

def main(): 

    while True:
        Menu()
        choice = int(input("Enter the choice: "))
        if choice == 1:
            Number = int(input("Enter the number: "))
            print(f"Square root of the {Number} is {math.sqrt(Number)}")
        elif choice == 2:
            print("Enter T for Traingle C for Cicle: ")
            cho = input().upper()
            if cho == 'T':
                print("Enter the Height and base of the traingle")
                Height = float(input("Enter the Height of the triangle: "))
                base = float(input("Enter the base of the triangle: "))
                s1 = float(input("Enter the side 1 of the triangle: "))
                s3 = float(input("Enter the value of third side: "))
                PeriT = (s1 + base + s3)
                Area = 0.5 * base * Height
                print(f"the Perimeter of the triangle is {PeriT} and Area is {Area}")
            elif cho == 'C':
                radius = float(input("enter the radius of the circle"))
                circum = 2 * math.pi * radius
                area = math.pi * radius**2
                print(f"The circumference of the circle is {circum} and area is {area}")
        elif choice == 3:
            a = float(input("enter the value  of a: "))
            b = float(input("enter the coeeficent of b: "))
            c = float(input("enter the value of c: "))
            d = b**2 - 4*a*c
            if d> 0:
                x0 = (-b + math.sqrt(d))/(2*a) 
                x1 = (-b - math.sqrt(d))/(2*a) 
                print("Two real roots: ")
                print(x0)
                print(x1)
            elif d == 0:
                y = -b/(2*a)
                print("one real root:")
                print(y)
            else:
                real = -b / (2*a)
                imag = math.sqrt(-d)/(2*a)
                print("Complex roots: ")
                print(real,"+",imag,"i")
                print(real,"-",imag,"i")
        elif choice == 4:
            num1 = float(input("Enter the value of the first Number: "))
            num2 = float(input("Enter the value of the Second number:"))
            print(f"the value of number 1 and number 2 before swapping:{num1},{num2}")  
            (num1,num2) = (num2,num1)
            print(f"the value of number 1 and number 2 after swapping: {num1},{num2}")
        elif choice == 5:
            Km = float(input("Enter the value in Kilometers: "))
            Miles = Km * 0.621371
            print(f"The distance in KM {Km} is equal to {Miles} miles") 
        elif choice == 6:
            celsius = float(input("Enter the temperature in Celsius: "))
            Fahrenheit = celsius*1.8 + 32
            print(f"The temperature in Celsius {celsius} is equal to {Fahrenheit} Fahrenheit")
        elif choice == 7:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice.")
if __name__ == "__main__":
    main()