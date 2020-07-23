#Write a function called copy_pointlessly. This function should
#take two parameters, both strings. The first string is the
#filename of a file to which to write (output_file), and the
#second string is the filename of a file from which to read
#(input_file).
#
#copy_pointlessly should copy the contents of input_file into
#output_file, but make the following changes:
#
# - Replace all instances of the letter A (either capital or
#   lower case) with the at sign, @
# - Replace all instances of the letter M (either capital or
#   lower case) with the character sequence |\/|
# - Replace all instances of the letter W with the character
#   sequence \/\/
# - Replace all instances of the letter O (either capital
#   or lower case) with the numeral 0
# - Alternate the case for every remaining letter in the
#   string (hint: the_string.swapcase() returns the string
#   with the case of all letters swapped)

def copy_pointlessly(output_file, input_file):
    OF = open(output_file, "w")
    IF = open(input_file, "r")
    for line in IF:
        line = line.strip()
        line = line.replace("A", "@")
        line = line.replace("a", "@")
        line = line.replace("M", "|\/|")
        line = line.replace("m", "|\/|")
        line = line.replace("W", "\/\/")
        line = line.replace("w", "\/\/")
        line = line.replace("O", "0")
        line = line.replace("o", "0")
        line = line.swapcase()
        print(line, file = OF)
    OF.close()
    IF.close()

#If your code works, anOutputFile.txt should have the text:
#TEST @N @, TEST @N @
#TEST @N 0, TEST @N 0
#TEST @N |\/|, TEST @N |\/|
#TEST @ \/\/, TEST @ \/\/
copy_pointlessly("anOutputFile.txt", "anInputFile.txt")
print("Done running! Check anOutputFile.txt for the result.")
