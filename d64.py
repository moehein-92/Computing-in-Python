def tire_pressure(intList):
    lst = intList[-10:]
    valid = []
    for i in lst:
        if i >= 15 and i<= 55:
            valid.append(i)
    avg = sum(valid)/len(valid)


    return avg



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 34.7
a_list = [34, 34, 64, 34, 5, 5, 34, 34, 35, 35, 35, 65, 60, 35, 12, 35]
print(tire_pressure(a_list))
