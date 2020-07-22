def sort_films(input_file, output_file):
    finput = open(input_file, "r")
    foutput = open(output_file, "w")
    superlist = []
    list = []
    for line in finput:
        r = line.split("\t")
        list = [r[0], r[1].strip()]
        list.reverse()
        superlist.append(list)
    superlist.sort()
    superlist.reverse()
    #print(superlist)
    for i in superlist:
        y = i[1]+"\t"+i[0]
        print(y, file = foutput)
    finput.close()
    foutput.close()

#The line of code below will test your function and put
#your results in top500result.txt. Then, it will print
#"Done!"
sort_films("top500.txt", "top500result.txt")
print("Done!")
