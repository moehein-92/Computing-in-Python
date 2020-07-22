def steps(x):
    tabs = 0
    num = 1
    string = ""
    for i in range(1, x+1):
        string += (tabs*"\t")+str(num)*3+"\n"
        tabs += 1
        num += 1
    return string

#print(steps(3))
#111
#	222
#		333
#
#print(steps(6))
#111
#	222
#		333
#			444
#				555
#					666
#
print(steps(3))
print(steps(6))
