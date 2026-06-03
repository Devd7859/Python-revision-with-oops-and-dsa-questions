# Character Analyzer & Weekday Management System

def alphabet():
    character = input("Enter a character: ")
    
    if character.isalpha():
        print("It is an alphabet.")
    else:
        print("It is not an alphabet.")
    print()


def string_checker():
    char = input("Enter a  character to classify: ")
    
    if char.isalpha():
        print("It is an Alphabet.")
    elif char.isdigit():
        print("It is a Digit.")
    else:
        print("It is a Special Character.")
    print()


def case_checker():
    char = input("Enter an alphabet character: ")
    
    if not char.isalpha():
        print("It is not a valid alphabet character.")
    elif char.isupper():
        print("It is an Uppercase alphabet.")
    elif char.islower():
        print("It is a Lowercase alphabet.")
    print()


def weekday():
    day = int(input("Enter a week number (1-7): "))
    
    if day == 1:
        print("Day 1 is Monday.")
    elif day == 2:
        print("Day 2 is Tuesday.")
    elif day == 3:
        print("Day 3 is Wednesday.")
    elif day == 4:
        print("Day 4 is Thursday.")
    elif day == 5:
        print("Day 5 is Friday.")
    elif day == 6:
        print("Day 6 is Saturday.")
    elif day == 7:
        print("Day 7 is Sunday.")
    else: 
        print("Enter a valid input between 1 to 7.")
    print()


if __name__ == "__main__":
    alphabet()
    string_checker()
    case_checker()
    weekday()