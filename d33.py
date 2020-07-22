def load_file(filename):
    inputFile = open(filename, "r")
    for line in inputFile:
        try:
            int(line)
            x = int(line.strip())
        except:
            try:
                float(line)
                x = float(line.strip())
            except:
                x = line.strip()
    inputFile.close()
    return x


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print 123, followed by <class 'int'>.
contents = load_file("LoadFromFileInput.txt")
print(contents)
print(type(contents))
