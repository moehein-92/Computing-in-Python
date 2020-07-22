def count_types(string):
    dic = {}
    upper_count = 0
    lower_count = 0
    numeral = 0
    punctuation = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    punct = 0
    spaces = 0
    for i in string:
        if ord(i) >=65 and ord(i) <=90:
            upper_count += 1
        if ord(i) >=97 and ord(i) <=122:
            lower_count += 1
        if ord(i) >=47 and ord(i) <=57:
            numeral += 1
        if i in punctuation:
            punct += 1
        if ord(i) == 32:
            spaces += 1

    dic["upper"] = upper_count
    dic["lower"] = lower_count
    dic["numeral"] = numeral
    dic["punctuation"] = punct
    dic["space"] = spaces

    return dic

#The types of characters that should be handled (and
#thus, the keys in the dictionary) are:
#
# - upper: the count of upper-case or capital letters
# - lower: the count of lower-case letters
# - punctuation: the count of punctuation characters.
#   You may assume this is limited to these punctuation
#   characters: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# - space: the count of spaces
# - numeral: the count of numerals, 0123456789
#
#Note, however, that any type of character that does
#NOT appear in the string should not be in the dictionary
#at all.
#
#For example:
#
#count_characters("aabbccc") ->
# {"lower": 7}
#count_characters("ABC 123 doe ray me!") ->
# {"upper": 3, "lower": 8, "punctuation": 1, "space": 4, "numeral": 3}
#
#Because the first string has only lower-case letters,
#"lower" is the only key in the dictionary.
#
#HINT: If you're sing the ord() function, capitals of
#ordinals between 65 and 90; lower-case letters have
#ordinals between 97 and 122; numerals are between 48
#and 57; spaces are 32; all other numbers between 33
#and 126 are punctuations, and no character will have
#an ordinal outside that range.


#Write your function here!



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print (although the order of the keys may vary):
#
#{"lower": 7}
#{"upper": 3, "lower": 8, "punctuation": 1, "space": 4, "numeral": 3}
print(count_types("aabbccc"))
print(count_types("ABC 123 doe ray me!"))
