f = open("poems.txt","r")
content = f.read()
if ('twinkle' in content):
    print("Twinkle is present in the content")
else:
    print("It is not present in the content")
f.close()
