#Write a function called delete_from_list. delete_from_list
#should have two parameters: a list of strings and a list of
#integers.
#
def delete_from_list(slist, indices):
    lst = []
    for i in indices:
        lst.append(slist[i])

    for j in lst:
        slist.remove(j)

    return slist

#The list of integers represents the indices of the items to
#delete from the list of strings. Delete the items from the
#list of strings, and return the resulting list.
#
#For example:
#
# delete_from_list(["a", "b", "c", "d", "e", "f"], [0, 1, 4, 5])
#
#...would return the list ["c", "d"]. "a" is at index 0, "b" at 1,
#"e" at 4, and "f" at 5, so they would all be removed.

print(delete_from_list(["a", "b", "c", "d", "e", "f"], [0, 1, 4, 5]))
print(delete_from_list(["a", "b", "c", "d", "e", "f"], [2, 3]))
print(delete_from_list(["Doppler", "franca", "CRT", "transatlantic", "designate", "brain", "plus", "derelict"], [2, 7, 1]))
