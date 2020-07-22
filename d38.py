def st_dev(filename):
    fopen = open(filename, "r")
    list1 = []
    for line in fopen:
        list1.append(int(line))
    mean = sum(list1)/(len(list1))
    sum_diff = 0
    for num in list1:
        diff = (int(num)-mean)**2
        sum_diff += diff
    #print(sum_diff)
    y = (sum_diff/len(list1))**0.5
    fopen.close()
    return y
# 1. Find the mean of the list.
# 2. For each data point, find the difference between that
#    point and the mean. Square that difference, and add it
#    to a running sum of differences.
# 4. Divide the sum of differences by the length of the
#    list.
# 5. Take the square root of the result.

#If your function works correctly, this will originally
#print 27.796382658340438 (or something around there).
print(st_dev("some_numbers.txt"))
