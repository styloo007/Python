def isAnagram(string,string1):
    map1 = {}
    map2 = {}

    for char in string:
        map1[char]=map1.get(char,0)+1
    
    for char2 in string1:
        map2[char2]=map2.get(char,0)+1
    
    count=0
    str = "abcdefghijklmnopqrstuvwxyz"


    for i in str:
        one = map1.get(i)
        two = map2.get(i)

        if(one==two):
            return 1
        
        return 0


string = input("Enter your string 1")
string1 = input("Enter your string 2")
print(isAnagram(string, string1))

