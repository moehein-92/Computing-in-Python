def write_1301(filename, tlist):
    fopen = open(filename, "w")
    for list in tlist:
        (assignment_num, exam_num, score, points, perc) = list
        y = str(assignment_num)+" "+str(exam_num)+" "+str(score)+" "+str(points)+" "+str(perc)
        print(y, file = fopen)
    fopen.close()




#The code below will test your function. It's not used
#for grading, so feel free to modify it! You may check
#output.cs1301 to see how it worked.
tuple1 = (1, "exam_1", 90, 100, 0.6)
tuple2 = (2, "exam_2", 95, 100, 0.4)
tupleList = [tuple1, tuple2]
write_1301("output.cs1301", tupleList)
