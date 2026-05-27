#Question 2 Banking utility System:
def menu():
    print("What do you will like to do: ")
    print("1: Deposit Amount: ")
    print("2: Withdraw Amount: ")
    print("3: Check Balance: ")
    print("4: Calculate Simple Interest: ")
    print("5: Calculate Compound Interest: ")
    print("6 Currency Convert:")
    print("7: Exit the program")
def main():
    Amount = 100000
    while True:
        menu()
        choice = int(input("enter your choice: "))
        if choice == 1:
            Amt = int(input("Enter the amount You want to Deposit: "))
            Amount += Amt
            print(f"After deposit {Amt} your bank balance is {Amount}")
        elif choice == 2:
            ded = int(input("Enter the amount you want to withdraw: "))
            if ded > Amount:
                print("Insufficient Balance.")
            else:
                Amount -= ded
                print(f"After withdrawing {ded} amount you have {Amount} in your bank balance")
        elif choice == 3:
            print(f"Your current bank Balance is {Amount}")
        elif choice == 4:
            Rate = float(input("enter the rate of interest: "))
            time = float(input("enter the time in years: "))
            principal = Amount
            SI = principal* time* Rate /100
            print(f"The simple interest after time {time} and rate {Rate} is {SI}")
        elif choice == 5:
            rate = float(input("enter the rate of interest: "))
            Time = float(input("enter the time in years: "))
            principal = Amount
            n = int(input("how many times interest is compounded per year: "))
            CI = principal * (1 + ((rate/100)/n))**(n*Time)
            interest = CI - principal
            print(f"the compound interest after time {Time} at Rate {rate} and being compunded {n} times per year is {interest}")
        elif choice == 6:
            rup = float(input("enter the amount in rupees: "))
            conv = int(input("enter 1 to convert in dollar, 2 to convert into Pound, 3 to convert into kenyan shilling: "))
            if conv == 1:
                convr = rup * 0.012
                print(f"the rupess {rup} is equal to {convr} dollars.")
            elif conv == 2:
                convr = rup * 0.0078
                print(f"the rupess {rup} is equal to {convr} pounds.")
            elif conv == 3:
                convr = rup * 1.35
                print(f"the rupees {rup} is equal to {convr} kenyan shilling.")
            else:
                print("Sorry conversation not avaliable.")
        elif choice == 7:
            print("exiting the program.")
            break
        else:
            print("Invalid choice.")
if __name__ == "__main__":
    main()