
# two_dimensional_booleans(a_superlist, True) -> [True, False, False]
# two_dimensional_booleans(a_superlist, False) -> [True, True, False]
#
#When use_and is True, then only the first sublist gets
#a value of True. When use_and is False, then the first
#and second sublists get values of True in the final
#list.
#
#Hint: This problem can be extremely difficult or
#extremely simple. Try to use your answer or our
#code from the sample answer in the previous problem --
#it can make your work a lot easier! You may even want
#to use multiple functions.

#Write your function here!
def one_dimensional_booleans(bool_list, use_and):

        if use_and == True:
            for i in bool_list:
                if bool_list[i] == False:
                    return False
                else:
                    return True
        else:
            for i in bool_list:
                if i == False:
                    return False
                else:
                    return True
    

def two_dimensional_booleans(superlist, use_and):
    result = []
    for list in superlist:
        if one_dimensional_booleans(list, use_and):
            result.append(True)
        else:
            result.append(False)
    return result

bool_superlist = [[True, True, True], [True, False, True], [False, False, False]]
print(two_dimensional_booleans(bool_superlist, True))
print(two_dimensional_booleans(bool_superlist, False))
