#Write a function called is_palindrome. The function should
#have one parameter, a string. The function should return
#True if the string is a palindrome, False if not.
#
#A palindrome is a sequence of letters that is the same
#forward and backward. For example, "racecar" is a
#palindrome. In determining whether a string is a palindrome
#or not, you should ignore punctuation, capitalization and
#spaces. For example, "Madam in Eden, I'm Adam" is a
#palindrome.
#
#You may assume that the only characters in the string will
#be letters, spaces, apostrophes, commas, periods, and
#question marks.

def is_palindrome(string):
    string = string.replace(" ", "")
    string = string.replace("?", "")
    string = string.replace(".", "")
    string = string.replace(",", "")
    string = string.replace("'", "")
    string = string.lower()
    #return string[::-1]
    return string == string[::-1]

#If your function works correctly, this will originally
#print: True, True, False, each on their own line.
print(is_palindrome("racecar"))
print(is_palindrome("Madam in Eden, I'm Adam"))
print(is_palindrome("Mister in Eden, I'm Eve"))
