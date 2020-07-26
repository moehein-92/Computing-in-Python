def lazy_encrypt(file1, file2, dic):
    f1 = open(file1, "w")
    f2 = open(file2)
    for line in f2:
        line = line.strip()
        line = line.translate(str.maketrans(dic))
        print(line, file = f1)


#Output:
#Horo is a protty simplo mossago ta oncrypt
#Whon it's oncryptod, it will laak difforont

print(lazy_encrypt("Here is a pretty simple message to encrypt", {"e": "o", "o": "a"}))
print(lazy_encrypt("When it's encrypted, it will look different", {"e": "o", "o": "a"}))
