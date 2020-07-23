#Pig Latin is a fictitious language. To translate a word into
#Pig Latin, you would take the consonants up until the first
#vowel, move them to the end, and add "ay" to the end.
#
#For example:
#
# pig -> igpay
# david -> avidday
# trash -> ashtray
# scram -> amscray
# translate -> anslatetray
#

def to_pig_latin(string):
    vowels = "aeiou"
    first = string[0]
    if first in vowels:
        string += "ay"
        return string
    else:
        for i in string:
            if i in vowels:
                index_value = string.index(i)
                break
        string = string[index_value:]+string[:index_value]+"ay"
        return string

#Write a function called to_pig_latin. to_pig_latin will take
#as input a single word, and return the Pig Latin version of
#the word.

print(to_pig_latin("pig"))
print(to_pig_latin("david"))
print(to_pig_latin("trash"))
print(to_pig_latin("scram"))
print(to_pig_latin("translate"))
