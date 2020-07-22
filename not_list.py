#Write a function called not_list. not_list should have two
#parameters: a list of booleans and a list of integers.
#
#The list of integers will represent indices for the list of
#booleans. not_list should switch the values of all the
#booleans located at those indices.

def not_list(boolist, indices):
    for i in indices:
        if boolist[i] == True:
            boolist[i] = False
        elif boolist[i] == False:
            boolist[i] = True
    return boolist

# bool_list = [True, False, False]
# index_list = [0, 2]
# not_list(bool_list, index_list) -> [False, False, True]
#
#After calling not_list, the booleans at indices 0 and 2
#have been switched.
#
#Note that it may be the case that the same index is present
#in the second twice. If this happens, you should switch the
#boolean at that index twice. For example:
#
# bool_list = [True, False, False]
# index_list = [0, 2, 2]
# not_list(bool_list, index_list) -> [False, False, False]
#
#2 is in index_list twice, so the boolean at index 2 is
#switched twice: False to True, then True back to False.

print(not_list([True, False, False], [0, 2]))
print(not_list([True, False, False], [0, 2, 2]))
