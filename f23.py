def sortString(a_string):
    lw_string = ""
    up_string = ""
    punct = ""
    spaces = 0
    if isinstance(a_string, str):
        for i in a_string:
            if ord(i)<= 122 and ord(i) >=97:
                lw_string = lw_string + i

            if ord(i)<= 90 and ord(i) >=65:
                up_string = up_string + i

            if ord(i)<= 64 and ord(i) >=33:
                punct = punct + i

            if ord(i) == 32:
                spaces += 1
        combined = up_string +"\n"+lw_string+"\n"+punct+"\n"+str(spaces)
        return combined
    else:
        return "Not a string!"

#print(sortString("Hello!!"))



#The line of code below will test your function. It is not
#used for grading, so feel free to modify it. As written,
#it should print:
#ZOMGHCS
#ello
#,1301!!
#2
print(sortString("ZOMG Hello, CS1301!!"))
