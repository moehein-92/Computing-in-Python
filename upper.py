#Write a function called to_upper_copy. This function should
#take two parameters, both strings. The first string is the
#filename of a file to which to write (output_file), and the
#second string is the filename of a file from which to read
#(input_file).
#
#to_upper_copy should copy the contents of input_file into
#output_file, capitalizing all letters (not just all words,
#each individual letter). You may use the .upper() method
#from the string class.
#
def to_upper_copy(file1, file2):
    f1 = open(file1, "w")
    f2 = open(file2)
    for line in f2:
        line = line.strip().upper()
        print(line, file = f1)


#For example, if these were the contents of input_file (the
#second parameter):
#
# This is some text. Yay text.
#
#Then to_upper_copy would write this text to output_file (the
#first parameter):
#
# THIS IS SOME TEXT. YAY TEXT.
#
#No other characters should be changed. Note that the file
#to be copied will have multiple lines of text.
#

#The code below will test your function. You can find the two
#files it references in the drop-down in the top left.
to_upper_copy("anOutputFile.txt", "anInputFile.txt")
print("Done running! Check anOutputFile.txt for the result.")
