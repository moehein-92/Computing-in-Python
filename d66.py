#Write a function called next_fib. next_fib should take
#have two parameters: a list of integers and a single integer.
#For this description, we'll call the single integer n.
#
#next_fib should modify the list to add the next n pseudo-
#Fibonacci numbers to the end of the sequence. A pseudo-
#Fibonacci number is the sum of the previous two numbers in
#the sequence, but in our case, the previous two numbers may
#not be the original numbers from the Fibonacci sequence.
#
#For example, if the original list given was:
#
def next_fib(list, n):

    while n>0:
        i = len(list)-1
        fib = list[i]+list[(i-1)]
        list.append(fib)
        n -= 1

    return list

# a_list = [5, 5, 10, 15, 25, 40, 65]
#
# Then next_fib(a_list, 3) would return:
#       [5, 5, 10, 15, 25, 40, 65, 105, 170, 275]
#
#All the original numbers in the list are still there, and
#three new ones have been added.
#
#You may assume the list parameter will always have at least
#two numbers.

#If your function works correctly, this will originally
#print:
#[5, 5, 10, 15, 25, 40, 65, 105, 170, 275]
a_list = [5, 5, 10, 15, 25, 40, 65]
print(next_fib(a_list, 3))
