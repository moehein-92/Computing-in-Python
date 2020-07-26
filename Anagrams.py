#Write a function called are_anagrams. The function should
#have two parameters, a pair of strings. The function should
#return True if the strings are anagrams of one another,
#False if they are not.
#
#Two strings are considered anagrams if they have only the
#same letters, as well as the same count of each letter. For
#this problem, you should ignore spaces and capitalization.
#
#So, for us: "Elvis" and "Lives" would be considered
#anagrams. So would "Eleven plus two" and "Twelve plus one".

def are_anagrams(string1, string2):
    string1 = string1.strip().lower()
    string1 = string1.replace(" ", "")
    string2 = string2.strip().lower()
    string2 = string2.replace(" ", "")
    dic1 = {}
    dic2 = {}
    for i in string1:
        if i in dic1:
            dic1[i] += 1
        else:
            dic1[i] = 1

    for j in string2:
        if j in dic2:
            dic2[j] += 1
        else:
            dic2[j] = 1

    if dic1 == dic2:
        return True
    else:
        return False

print(are_anagrams("Elvis", "Lives"))
print(are_anagrams("Elvis", "Live Viles"))
print(are_anagrams("Eleven plus two", "Twelve plus one"))
print(are_anagrams("Nine minus seven", "Five minus three"))
print(are_anagrams("Astronomer", "Moon Starer"))
