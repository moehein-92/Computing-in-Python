#In this file, each component will meet the following
#description:
#
# - number: an integer-like value of the assignment number
#
# - assignment_name: a string value of the assignment name
#
# - grade: an integer-like value of a student’s grade
#
# - total: an integer-like value of the total possible
#   number of points
#
# - weight: a float-like value ranging from 0 to 1
#   representing the percent of the student’s grade this
#   assignment is worth. All the weights should add up to 1.
#
def format_checker(fname):
    fopen = open(fname, "r")
    add_1 = []
    for line in fopen:
        list = line.split()
        if len(list) == 5:
            try:
                first = int(list[0])
                second = int(list[2])
                fourth = int(list[3])
                fifth = float(list[4])
            except:
                fopen.close()
                return False
            else:
                add_1.append(fifth)
        else:
            fopen.close()
            return False
    if not sum(add_1) == 1:
        fopen.close()
        return False
    fopen.close()
    return True
#Write a function called format_checker that accepts a
#filename and returns True if the file contents accurately
#conform to the described format. Otherwise the function
#should return False. In other words, it should return True
#if:
#
# - Each line has five elements separated by spaces, AND
# - The first, third, and fourth elements are integers, AND
# - The fifth element is a decimal number, AND
# - All the fifth elements add to 1.
#
#You can make changes to test.cs1301 to test your function,
#or test it with sample.cs1301. Right now, running it on
#sample.cs1301 should return True, and on test.cs1301
#should return False.
#
#Hint 1: .split() will likely help separate each line into
#its components.
#Hint 2: .split() returns a list. So, if you were to do
#something like say split_line = line.split(), then
#split_line[0] would give the first item, split_line[1] would
#give the second item, etc.
#Hint 3: If you're having trouble, try breaking it down by
#parts. First check the file to see if it has the right
#number of items per line, then whether the items are of
#the correct type, then whether the fifth elements add to
#1. Remember, you know how to do each individual check
#(checking types, adding numbers, finding list lengths) --
#the hard part is knitting this all together into one bigger
#solution.


#Write your function here!



#Test your function below. With the original values of these
#files, these should print True, then False:
print(format_checker("sample_1.cs1301"))
print(format_checker("sample_2.cs1301"))
