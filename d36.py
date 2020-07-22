def angry_file_finder(filename):
    fopen = open(filename, "r")
    content = fopen.readlines()
    for line in content:
        if not "!" in line:
            return False
    return True
    fopen.close()


#If your function works correctly, this will originally
#print: True
print(angry_file_finder("AngryFileFinderInput.txt"))
