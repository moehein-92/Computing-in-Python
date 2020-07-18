def linear(lst, goal):
    for i in range(len(lst)):
        if lst[i] == goal:
            return i
        else:
            pass
    return False

#If your function works correctly, this will originally
#print: 3
a_list = [5, 1, 3, 6, 7, 3, 1, 6, 7, 8, 3, 6]
print(linear(a_list, 6))
