from datetime import date

def binary_search_year(lst, y):
    lst.sort()
    if len(lst) == 0:
        return False
    mid = len(lst)//2
    if lst[mid].year == y:
        return True
    else:
        if y < lst[mid].year:
            return binary_search_year(lst[:mid], y)
        elif y > lst[mid].year:
            return binary_search_year(lst[mid+1:], y)


#If your function works correctly, this will originally
#print: True, then False
listOfDates = [date(2016, 11, 26), date(2014, 11, 29),
               date(2008, 11, 29), date(2000, 11, 25),
               date(1999, 11, 27), date(1998, 11, 28),
               date(1990, 12, 1), date(1989, 12, 2),
               date(1985, 11, 30)]

print(binary_search_year(listOfDates, 2016))
print(binary_search_year(listOfDates, 2007))
