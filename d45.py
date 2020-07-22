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

def get_grade(fname):
    lists = reader(fname)
    results = 0
    for list in lists:
        grade = (list[2]/list[3])*list[4]
        results += grade
    result = results*100
    return result

print(get_grade("sample.cs1301"))
