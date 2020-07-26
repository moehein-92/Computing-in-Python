#Create a class called Name. Name should have two attributes
#(instance variables): first_name and last_name. Make sure
#the variable names match those words. Both will be strings.
#
class Name:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def find_printed_name(self):
        return "{0} {1}".format(self.first_name, self.last_name)

    def find_sortable_name(self):
        return "{0}, {1}".format(self.last_name, self.first_name[0])

#If your function works correctly, this will originally
#print
#David
#Joyner
#David Joyner
#Joyner, D
test_name = Name("David", "Joyner")
print(test_name.first_name)
print(test_name.last_name)
print(test_name.find_printed_name())
print(test_name.find_sortable_name())
