#p1 Smart Number Filter & Banking Validation System.
def filter_number():
    results =[]
    for i in range(2000,3200,1):
        if(i % 7 == 0 and i % 5 != 0):
            results.append(str(i))
    print(",".join(results))
    print()
def Transaction_checker():
    number = int(input("Enter the transaction number: "))
    if number % 5 == 0 and number % 11 == 0:
        print(f"The {number} is divisible by both 5 and 11.")
    else:
        print(f"The {number} is not divisible by 5 and 11.")
def amount_checker():
    amount = int(input("Enter the Amount:"))
    notes = [500,200,100,50,20,10,5,2,1]
    remain = amount
    total_notes = 0
    notes_breakdown = {}
    for note in notes:
        if remain >= note:
            count = remain // note
            remain %= note
            total_notes += count
            notes_breakdown[note] = count
    print(f"the total number of notes required: {total_notes}")
    print("Breakdown:")
    for note,count in notes_breakdown.items():
       print(f"  ₹{note} x {count}")
if __name__ == "__main__":
    filter_number()
    Transaction_checker()
    amount_checker()
