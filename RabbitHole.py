#Write a function called rabbit_hole. rabbit_hole should have
#two parameters: a dictionary and a string. The string may be
#a key to the dictionary. The value associated with that key,
#in turn, may be another key to the dictionary.
#
#Keep looking up the keys until you reach a key that has no
#associated value. Then, return that key.
def rabbit_hole(dic, string):
    try:
        if not string in dic:
            return string
        else:
            return rabbit_hole(dic, dic[string])
    except:
        return False
        
#For example, imagine if you had the following dictionary.
#This one is sorted to make this example easier to follow:
#
# d = {"bat": "pig", "pig": "cat", "cat": "dog", "dog": "ant",
#      "cow": "bee", "bee": "elk", "elk": "fly", "ewe": "cod",
#      "cod": "hen", "hog": "fox", "fox": "jay", "jay": "doe",
#      "rat": "ram", "ram": "rat"}
#
#If we called rabbit_hole(d, "bat"), then our code should...
#
# - Look up "bat", and find "pig"
# - Look up "pig", and find "cat"
# - Look up "cat", and find "dog"
# - Look up "dog", and find "ant"
# - Look up "ant", and find no associated value, and so it would
#   return "ant".

#Note, however, that it is possible to get into a loop. In the
#dictionary above, rabbit_hole(d, "rat") would infinitely go
#around between "rat" and "ram". You should prevent this: if a
#key is ever accessed more than once (meaning a loop has been

d = {"bat": "pig", "pig": "cat", "cat": "dog", "dog": "ant",
     "cow": "bee", "bee": "elk", "elk": "fly", "ewe": "cod",
     "cod": "hen", "hog": "fox", "fox": "jay", "jay": "doe",
     "rat": "ram", "ram": "rat"}

print(rabbit_hole(d, "bat"))
print(rabbit_hole(d, "ewe"))
print(rabbit_hole(d, "jay"))
print(rabbit_hole(d, "yak"))
print(rabbit_hole(d, "rat"))
