username = input("enter the username: ")
if len(username)<10:
    print("it containus less than 10 characters.")
elif len(username) == 10:
    print("equal to  10 characters.")
else:
    print("more than 10 characters.")