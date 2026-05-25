list = ["harry", "dev" , "chetanya","khushi"]
n = len(list)
name = input("enter the name to check if it is present in it or not: ")

if name in list:
    print("{0} found in the list".format(name))
else:
    print("{0} not found in the list".format(name))

