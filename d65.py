#Write a function called find_median. find_median
#should take as input a string representing a filename.
#The file corresponding to that filename will be a list
#of integers, one integer per line. find_median should
#return the median of the numbers in the file.
#
#If there is an odd number of values in the file, then
#find_median will return the middle value from the numbers
#in the file after they're sorted.
#
def find_median(string):
    fopen = open(string, "r")
    numList = []
    for i in fopen:
        numList.append(i)
    numList.sort()
    if len(numList) % 2 == 1:
        median = numList[len(numList)/2]
        return median
    elif len(numList) %2 == 0:
        index1 = len(numList)//2
        index2 = index1 - 1
        median = (numList[index1]+numList[index2])/2
        return median

#If there is an even number of values in the file, then
#find_median should return the average of the two middle
#values after they're sorted.

#If your function works correctly, this will originally
#print: 16
print(find_median("FindMedianInput.txt"))
