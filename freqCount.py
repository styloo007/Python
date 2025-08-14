def FreqCount(a):
    a=a.lower()
    count = {}
    for char in a:
        count[char]=count.get(char,0)+1

    print(count)


a=input("Enter the String")
print(FreqCount(a))