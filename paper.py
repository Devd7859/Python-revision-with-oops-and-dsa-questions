'''
with open("output.txt","w") as f:
    f.write("Hello! this is the first line of the text.\n")
    f.write("Python file handling is simple and fun.\n")
    f.write("This is the final line stored in the file.")

with open("output.txt","r") as f:
    content = f.read()
    print(content)

file_name = input("Enter the name of the text file: ")
keyword = input("Enter the keyword you want to check.")
with open("file_name.txt","r") as f:
    content = f.read()
lowercased_content = content.lower()
lowercased_keyword = keyword.lower()
occurrences = lowercased_content.count(lowercased_keyword)
print(f"the keyword {keyword} appears {occurrences} times.")

sentence = "tHiS IS gOING To bE easy"
result = ""
capitalize_text = True
for char in sentence:
    if char == " ":
        capitalize_text = True
        continue
    else:
        ascii_val = ord(char)
        if capitalize_text:
            if 97<= ascii_val <= 122:
                char = chr(ascii_val - 32)
            capitalize_text = False
        else:
            if 65 <= ascii_val <= 90:
                char = chr(ascii_val + 32)
    result += char
print("Sample Output: ", result)

products = [
    {'name':'Laptop', 'quantity' : 10,'price':700 },
    {'name': 'Phone', 'quantity' : 50, 'price' : 300},
    {'name' : 'Table', 'quantity' : 30, 'price' : 250}
]
with open('products.txt', 'w') as f:
    for prod in products:
        name = prod['name']
        quantity = prod['quantity']
        price = prod['price']
        f.write(f"{name},{quantity},{price}\n")
print("Product details successfully saved to 'product.txt'. ")

with open("input.txt","w") as f:
    print("Enter multiple lines of text (press Enter on a blank line to stop.)")
    while True:
        line = input()
        if line == "":
            break
        f.write(line + "\n")
with open("input.txt","r") as f:
    content = f.read()
    words = content.split()
    longest = ""
    for word in words:
        if len(word) >= len(longest):
            longest = word
    print(f"The longest word in the file is: {longest}")

def dup(strr):
    newstrr =""
    for char in strr:
        if char not in newstrr:
            newstrr += char
    return newstrr

input_string = input("Enter the string: ")
output_string = dup(input_string)
print(f"input: {input_string}")
print(f"output: {output_string}")
'''
import re
text = "My marks are 85,90 and 78"
result = re.findall(r"m\w+",text)
print(result)