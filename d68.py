#APA citation style cites author names like this:
#
#  Last, F., Joyner, D., & Burdell, G.
#
def names_to_apa(names):
    names = names.replace(', and ', ', ')
    names = names.split(', ')
    names = [name.split() for name in names]
    names = [name[-1]+', '+(''.join(initial[0]+'.' for initial in name[:-1])) for name in names]
    #print(names)
    names = ', '.join(names[:-1])+', & '+names[-1]
    return names


#If your function works correctly, this will originally
#print: Last, F., Joyner, D., & Burdell, G.
print(names_to_apa("First Last, David Joyner, and George Burdell"))
