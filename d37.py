def average_file(file):
    fname = open(file, "r")
    lst = []
    for line in fname:
        try:
            x = int(line)
            lst.append(x)
        except:
            fname.close()
            return "Error reading file!"
    avg = sum(lst)/len(lst)
    fname.close()
    return avg

#If your function works correctly, this will originally
#print: 5.0, then Error reading file!

print(average_file("valid_file.txt"))
print(average_file("invalid_file.txt"))
