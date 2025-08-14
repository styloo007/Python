def CountFreq(a):
    a=a.lower()
    list = [0]*256
    for char in a:
        list[ord(char)]+=1
    

    for i in range(256):
        if(list[i]!=0):
            print(chr(i),list[i])

a = input("Enter the String")
CountFreq(a)
