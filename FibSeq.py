class FibSeq:
    def __init__(self):
        self.back1 = 1
        self.back2 = 0
    def next_number(self):
        next = self.back1+self.back2
        self.back2 = self.back1
        self.back1 = next
        return next

#The code below will test your method. It's not used for
#grading, so feel free to change it. As written, it should
#print 1, 2, 3, 5, and 8.
newFib = FibSeq()
print(newFib.next_number())
print(newFib.next_number())
print(newFib.next_number())
print(newFib.next_number())
print(newFib.next_number())
