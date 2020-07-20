def generate_name(filename, name):
    fopen = open(filename, "r")
    name_list = []
    name = name.split()
    for line in fopen:
        line = line.strip()
        name_list.append(line)
    mid = len(name_list)//2
    first_names = name_list[:mid]
    last_names = name_list[mid:]

    first_ord = ord(name[0][0])
    last_ord = ord(name[1][0])
    output = []
    if first_ord == 65:
        output.append(first_names[0])
    elif first_ord == 66:
        output.append(first_names[1])
    elif first_ord == 67:
        output.append(first_names[2])
    elif first_ord == 68:
        output.append(first_names[3])
    elif first_ord == 69:
        output.append(first_names[4])
    elif first_ord == 70:
        output.append(first_names[5])
    elif first_ord == 71:
        output.append(first_names[6])
    elif first_ord == 72:
        output.append(first_names[7])
    elif first_ord == 73:
        output.append(first_names[8])
    elif first_ord == 74:
        output.append(first_names[9])
    elif first_ord == 75:
        output.append(first_names[10])
    elif first_ord == 76:
        output.append(first_names[11])
    elif first_ord == 77:
        output.append(first_names[12])
    elif first_ord == 78:
        output.append(first_names[13])
    elif first_ord == 79:
        output.append(first_names[14])
    elif first_ord == 80:
        output.append(first_names[15])
    elif first_ord == 81:
        output.append(first_names[16])
    elif first_ord == 82:
        output.append(first_names[17])
    elif first_ord == 83:
        output.append(first_names[18])
    elif first_ord == 84:
        output.append(first_names[19])
    elif first_ord == 85:
        output.append(first_names[20])
    elif first_ord == 86:
        output.append(first_names[21])
    elif first_ord == 87:
        output.append(first_names[22])
    elif first_ord == 88:
        output.append(first_names[23])
    elif first_ord == 89:
        output.append(first_names[24])
    elif first_ord == 90:
        output.append(first_names[25])


    if last_ord == 65:
        output.append(last_names[0])
    elif last_ord == 66:
        output.append(last_names[1])
    elif last_ord == 67:
        output.append(last_names[2])
    elif last_ord == 68:
        output.append(last_names[3])
    elif last_ord == 69:
        output.append(last_names[4])
    elif last_ord == 70:
        output.append(last_names[5])
    elif last_ord == 71:
        output.append(last_names[6])
    elif last_ord == 72:
        output.append(last_names[7])
    elif last_ord == 73:
        output.append(last_names[8])
    elif last_ord == 74:
        output.append(last_names[9])
    elif last_ord == 75:
        output.append(last_names[10])
    elif last_ord == 76:
        output.append(last_names[11])
    elif last_ord == 77:
        output.append(last_names[12])
    elif last_ord == 78:
        output.append(last_names[13])
    elif last_ord == 79:
        output.append(last_names[14])
    elif last_ord == 80:
        output.append(last_names[15])
    elif last_ord == 81:
        output.append(last_names[16])
    elif last_ord == 82:
        output.append(last_names[17])
    elif last_ord == 83:
        output.append(last_names[18])
    elif last_ord == 84:
        output.append(last_names[19])
    elif last_ord == 85:
        output.append(last_names[20])
    elif last_ord == 86:
        output.append(last_names[21])
    elif last_ord == 87:
        output.append(last_names[22])
    elif last_ord == 88:
        output.append(last_names[23])
    elif last_ord == 89:
        output.append(last_names[24])
    elif last_ord == 90:
        output.append(last_names[25])

    " ".join(output)
    fopen.close()
    return output

#print: Captain Hawk, Doctor Yellow Jacket, and Moon Moon,
#each on their own line.
print(generate_name("heronames.txt", "Addison Zook"))
print(generate_name("heronames.txt", "Uma Irwin"))
print(generate_name("heronames.txt", "David Joyner"))
