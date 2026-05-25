sub1 = int(input("enter the marks of the first subject: "))
sub2 = int(input("enter the marks of the second subject: "))
sub3 = int(input("enter the marks of the third subject: "))
total = sub1 + sub2 + sub3
total_perct = total / 300 * 100
if(total_perct< 40):
    print("fail")
else:
    if(sub1<33):
        print("fail1")
    elif(sub2<33):
        print("fail2")
    elif(sub3<33):
        print("fail3")
    else:
        print("you have passed the exam.")
