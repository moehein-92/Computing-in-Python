def cap_count(a_string):
    cap_count = 0
    for i in a_string:
        if ord(i)<= 90 and ord(i) >=65:
            cap_count += 1
    return cap_count

def low_count(a_string):
    low_count = 0
    for i in a_string:
        if ord(i)<= 122 and ord(i) >=97:
            low_count += 1
    return low_count

def num_count(a_string):
    num_count = 0
    numbers = "0123456789"
    for i in a_string:
        if i in numbers:
            num_count += 1
    return num_count

def punct_check(a_string):
    punct1 = "!@#$%&()-_[]{};':,/.<>?"
    punct2 = '"'
    for i in range(0, len(a_string)):
        if (a_string[i] in punct1) or (a_string[i] in punct2):
            return True
        else:
            return False

def check_space(a_string):
    space_count = 0
    for i in a_string:
        if i == " ":
            space_count += 1
    return space_count

def password_check(a_string):
    if len(a_string)>= 8:
        if (cap_count(a_string)>=1) and (low_count(a_string)>=1)\
        and (num_count(a_string)>=1) and (punct_check(a_string))\
        and (check_space(a_string) == 0):
            return True
        else:
            return False
    else:
        return False

#print: True, True, False, False, False
print(password_check("tHIs1sag00d.p4ssw0rd."))
print(password_check("3@t7ENZ((T"))
print(password_check("2.shOrt"))
print(password_check("all.l0wer.case"))
print(password_check("inv4l1d CH4R4CTERS~"))


print(password_check("}!4j kZSG"))
