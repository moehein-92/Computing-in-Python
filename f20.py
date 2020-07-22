
#  numCombinations = n! / r!(n-r)!

def factorial(x):
    fact = 1
    for i in range(1, x+1):
        fact = fact*i
    return fact

def numCombinations(n, r):
    numCombo = factorial(n)/(factorial(r)*(factorial(n-r)))
    return numCombo


#The lines below will test your code. They are not used for
#grading, so feel free to modify them. As written, they should
#print: 1326.0, 252.0, and 4.0, each on their own line.
print(numCombinations(52, 2))
print(numCombinations(10, 5))
print(numCombinations(4, 1))
