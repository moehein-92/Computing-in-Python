#Write a function called most_oscars, which takes in one
#parameter, a dictionary. This dictionary maps names to the
#number of Academy Awards for which they have been nominated.
#This function should return a tuple containing the name and
#number of nominations for the person who has the most
#nominations.
#
#You may assume there will not be a tie for the actor with
#the most nominations (although there may be other ties in
#the list).
def most_oscars(dic):
    max = 0
    for (k, v) in dic.items():
        if v > max:
            max = v
            tuple = (k, v)
    return tuple


#If your function works correctly, this will originally
#print: ('Meryl Streep', 20)
nominees = {'Meryl Streep': 20, 'Robert De Niro': 7, 'Michael Caine': 6, 'Maggie Smith': 6}
print(most_oscars(nominees))
