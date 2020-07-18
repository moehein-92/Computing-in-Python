def sort_with_select(a_list):

    for i in range(len(a_list)):
        minIndex = i

        for j in range(i + 1, len(a_list)):
            if a_list[j] < a_list[minIndex]:
                minIndex = j
                print(minIndex)

        minValue = a_list[minIndex]
        del a_list[minIndex]
        a_list.insert(i, minValue)
    return a_list


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: [1, 2, 3, 4, 5]
print(sort_with_select([5, 3, 1, 2, 4]))
