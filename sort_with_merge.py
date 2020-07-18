def sort_with_merge(lst):
    if len(lst) <= 1:
        return lst
    else:
        midpoint = len(lst) // 2
        #print(midpoint)
        left = sort_with_merge(lst[:midpoint])
        #print(left)
        right = sort_with_merge(lst[midpoint:])
        #print(right)
        newlist = []
        while len(left) and len(right) > 0:
            if left[0] > right[0]:
                newlist.append(left[0])
                del left[0]
            else:
                newlist.append(right[0])
                del right[0]
        newlist.extend(left)
        newlist.extend(right)
        return newlist

#will print [5, 3, 1, -1, -3, -5].
print(sort_with_merge([1, 3, -1, -3, -5, 5]))
