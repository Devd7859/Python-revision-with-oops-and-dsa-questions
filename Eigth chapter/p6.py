def rem(l,word):
    n = []
    for item in l:
        if item != word:
            n.append(item.strip(word))
    return n
l = ["harry","shubham","kajal","an"]
print(rem(l,"an"))
