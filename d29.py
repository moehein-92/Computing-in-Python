#  string_splitter("Hello world") -> ['Hello', 'world']

def string_splitter(string):
    words = []
    word = ""
    for i in string:
        if not i == " ":
            word += i
            #print(word)
        else:
            words.append(word)
            word = ""
    words.append(word)
    return words



#If your function works correctly, this will originally
#print: ['Hello', 'world']
print(string_splitter("Hello world"))
