def reader(fname):
    fopen = open(fname, "r")
    result = []
    for line in fopen:
        list = line.split()
        try:
            list[0] = int(list[0])
            list[2] = int(list[2])
            list[3] = int(list[3])
            list[4] = float(list[4])
        except:
            fopen.close()
            print("Error")
        else:
            y = (list[0], list[1], list[2], list[3], list[4])
            result.append(y)
    fopen.close()
    return result

#If your function works correctly, this will originally
#print:
#[(1, 'assignment_1', 85, 100, 0.25), (2, 'test_1', 90, 100, 0.25), (3, 'exam_1', 95, 100, 0.5)]
print(reader("sample.cs1301"))
