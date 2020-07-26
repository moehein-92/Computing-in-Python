#Write a function called alter_list. alter_list should have
#two parameters: a list of strings and a list of integers.
#
#The list of integers will represent indices for the list of
#strings. alter_list should alter the capitalization of all
#the words at the designated indices. If the word was all
#capitals, it should become all lower case. If it was all
#lower case, it should become all capitals. You may assume
#that the words will already be all-caps or all-lower case.
#
def alter_list(slist, indices):

    for i in indices:
        if slist[i].isupper():
            slist[i] = slist[i].lower()
        elif slist[i].islower():
            slist[i] = slist[i].upper()

    return slist

# string_list = ["hello", "WORLD", "HOW", "are", "you"]
# index_list = [0, 2]
# alter_list(string_list, index_list) ->
#                ["HELLO", "WORLD", "how", "are", "you"]
#
#After calling alter_list, the strings at indices 0 and 2
#have switched their capitalization.
#
#Note that it may be the case that the same index is present
#in the second twice. If this happens, you should switch the
#text at that index twice.

print(alter_list(["hello", "WORLD", "HOW", "are", "you"], [0, 2]))
