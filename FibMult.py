def fib_mult(n):
    if n == 1:
        return 1
    elif n == 2 or n == 3:
        return 2
    else:
        return fib_mult(n-1)*fib_mult(n-2)

#The lines below will test your code. If your funciton is
#correct, they will print 1, 2, 2, and 2097152.
print(fib_mult(1))
print(fib_mult(2))
print(fib_mult(3))
print(fib_mult(9))
