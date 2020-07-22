def length_words(string):
    string = string.lower()
    repl = ",.?!"
    for i in repl:
        string = string.replace(i, "")
    string = string.split()
    dic = {}
    #print(string)
    for word in string:
        word_length = len(word)
        dic[word_length] = []

        if word_length in dic:
            dic[word_length].append(word)
    return dic


print(length_words("I ate a bowl of cereal out of a dog bowl today."))
