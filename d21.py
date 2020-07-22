#Write a function called modify_list.

def modify_list(a_list):
    a_list.sort()
    a_list.reverse()
    a_list = a_list[:(len(a_list)-3)]
    if 7 in a_list:
        a_list.remove(7)
    a_list[0] = a_list[0]*2
    a_list[2] = a_list[2]*2
    return a_list
# - Sort the list (using the default sort method).
# - Reverse the order of the list.
# - Delete the last three items of the list.
# - Removes one instance the integer 7 from the list, if
#   it's present.
# - Double the values of the first and third items in
#   the list.
#If your function works correctly, this will originally
#print:
#[178, 81, 75.0, 4, 3.141592653589793, 3]
import math
print(modify_list([7, 4, 3, 2.0, 81, 37.5, 89, math.pi, -2, math.e]))
