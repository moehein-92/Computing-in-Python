def write_weird_file(filename, list, mode = "w", sort_first = False, reverse_first = False):
    fopen = open(filename, mode)
    if sort_first == True and reverse_first == True:
        list.sort()
        list.reverse()
    elif reverse_first == True:
        list.reverse()
    elif sort_first == True:
        list.sort()
    for items in list:
        print(items, file = fopen)
    fopen.close()

#Wait, where'd the other text go?
#It's gone!
#3
#2
#1
write_weird_file("output.txt", ["Hmm, I bet this text will disappear.", "I wonder where it will go?"])
write_weird_file("output.txt", ["Wait, where'd the other text go?", "It's gone!"])
write_weird_file("output.txt", [2, 1, 3], mode="a", sort_first=True, reverse_first=True)
