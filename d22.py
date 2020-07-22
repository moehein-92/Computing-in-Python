def multiply_strings(list):
    for i in range(0 , len(list)):
        if i%2 == 0:
            list[i] *= 2
    for i in range(0, len(list)):
        if i%3 == 0:
            list[i] *=3
    return list

#If your function works correctly, this will originally
#print:
#['AAAAAA', 'B', 'CC', 'DDD', 'EE', 'F', 'GGGGGG']
test_list = ["A", "B", "C", "D", "E", "F", "G"]
print(multiply_strings(test_list))
