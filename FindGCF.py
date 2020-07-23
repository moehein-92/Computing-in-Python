#The Greatest Common Factor (GCF) of two numbers is the
#largest number that divides evenly into those two
#numbers. For example, the Greatest Common Factor of 48
#and 18 is 6. 6 is the largest number that divides evenly
#into 48 (48 / 6 = 8) and 18 (18 / 6 = 3).
#
#Write a function called find_gcf. find_gcf should have
#two parameters, both integers. find_gcf should return
#the greatest common factor of those two numbers.
#
def find_gcf(n1, n2):
    num_list = list(range(1, 100))
    lst = []
    for i in num_list:
        if n1%i == 0 and n2%i == 0:
            lst.append(i)
    return max(lst)

#For example:
#
# find_gcf(48, 18) -> 6
# find_gcf(21, 7) -> 7
# find_gcf(47, 17) -> 1
#
#If one number is a multiple of the other, the greatest
#common factor is the smaller number (e.g. 21 and 7). If
#the numbers have no common factors, then their greatest
#common factor is 1 (e.g. 47 and 17).

print(find_gcf(48, 18))
print(find_gcf(21, 7))
print(find_gcf(47, 17))
print(find_gcf(72, 60))
print(find_gcf(60, 90))
