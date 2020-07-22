#Write a function called word_lengths, which takes in one
#parameter, a string, and returns a dictionary where each
#word of the string is mapped to an integer representing how
#how long that word is. You should ignore punctuation, and
#all the words should be lowercase. You can assume that the
#only punctuation marks in the string will be periods,
#commas, question marks, exclamation points, and apostrophes.
#
#For example:
#  word_lengths("I ate a bowl of cereal out of a dog bowl today.")
#  -> {'i':1, 'bowl':4, 'today':5, 'out':3, 'dog':3, 'ate':3,
#      'a':1, 'of':2, 'cereal':6}

def word_lengths(string):
    string = string.lower()
    string = string.replace(",", "")
    string = string.replace(".", "")
    string = string.replace("?", "")
    string = string.replace("!", "")
    string = string.split()

    string_length = []
    new_string = []
    for i in string:
        string_length.append(len(i))
        new_string.append(i)
    dic = {}
    dic = dict(zip(new_string, string_length))
    return dic


#If your function works correctly, this will originally
#print:
#{'dog': 3, 'today': 5, 'of': 2, 'ate': 3, 'bowl': 4, 'out': 3, 'a': 1, 'cereal': 6, 'i': 1}
#
#The order of the keys may differ, but that's okay!
print(word_lengths("I ate a bowl of cereal out of a dog bowl today."))
