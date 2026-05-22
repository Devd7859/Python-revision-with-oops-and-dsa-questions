friends = ["apples","orangers",5,345.06,False,"Aakash","Rohan"]
print(friends[0])
friends[0] = "grapes" #unlike strings lists are muttable
print(friends[0])
#list can be indexed like a string
#list can be sliced the same way as string can be
print(friends[0:4])
#list Methods
#append adding value at the last
friends.append("Dev")
print(friends)
l1 = [1,34,74,8,21,63,67]
x = sorted(l1) # or you should only do l1.sort() then print l1 both will give the same outputs
y = list(reversed(l1)) # or you can put l1.reverse() then print l1 both will give the same outputs
print(y)
print(x)
l1.insert(3,333333) #basically the difference between append and insert is that you can mention the index at which the value you want to add whereelse in append it will directly be inserted at the end only
l1.pop() #default it will remove the last index element of the list otherwise if you mention the index it will remove that index value 
l1.remove(74) #
print("updated l1: ", l1)