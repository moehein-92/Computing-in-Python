#Write your function here!
def mock(string):
    s = ""
    index = 0
    for i in string:
        if index%2 == 0:
            if ord(i) >= 32 and ord(i) <= 64:
                s += i
            elif ord(i) <= 122 and ord(i) >= 97:
                s += i.upper()
            elif ord(i) <= 90 and ord(i) >= 65:
                s += i.lower()
        else:
            s += i
        index+= 1
    return s

#If your function works correctly, this will originally
#print: "abCd. efGh.. IJkL!".

print(mock("Abcd. Efgh.. Ijkl!"))
