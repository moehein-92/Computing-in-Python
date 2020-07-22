
#The keys of the top-level dictionary should be the
#assignment names. Then, the value for each of those keys
#should be a dictionary with four keys: "number", "grade",
#"total", and "weight". The values corresponding to each of
#those four keys should be the values from the file,
#converted to the corresponding data types (ints or floats).
#
#For example, if the input file read:
#
# 1 exam_1 90 100 0.6
# 2 exam_2 95 100 0.4
#
#Then reader would return this dictionary of dictionaries:
#
# {"exam_1": {"number": 1, "grade": 90, "total": 100, "weight": 0.6},
#  "exam_2": {"number": 2, "grade": 95, "total": 100, "weight": 0.4}}

def reader(fname):
    fopen = open(fname, "r")
    result = {}
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
            result[list[1]] = {}
            result[list[1]]["number"] = list[0]
            result[list[1]]["grade"] = list[2]
            result[list[1]]["total"] = list[3]
            result[list[1]]["weight"] = list[4]

    fopen.close()
    return result

print(reader("sample.cs1301"))
