
def measure_string(myStr):
    if myStr == "":
    	return 0
    else:
        return 1 + measure_string(myStr[:-1])


#The line below will test your function. As written, this
#should print 13. You may modify this to test your code.
print(measure_string("13 characters"))
