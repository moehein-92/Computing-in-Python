
def insertion(lst):
    for i in range(1, len(lst)):
        temp = lst[i]
        j = i-1
        while j>= 0 and temp < lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = temp
    return lst


#The code below will test your function. If your function
#works, it will print: [1, 2, 3, 4, 5].
print(insertion([5, 1, 3, 2, 4]))
