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
    punct1 = "!@#$%&()-_[]{};'`:,/.<>?"
    punct2 = '"'
    check = True
    for i in range(0, len(a_string)):
        if (a_string[i] in punct1) or (a_string[i] in punct2):
            check = False
    return check

def check_space(a_string):
    space_count = 0
    for i in a_string:
        if i == " ":
            space_count += 1
    return space_count

def product_code_check(a_string):
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
print(product_code_check("g00dlONGproductCODE"))
print(product_code_check("fRV53FwSXX663cCd"))
print(product_code_check("2shOrt"))
print(product_code_check("alll0wercase"))
print(product_code_check("inv4l1d CH4R4CTERS~"))
print(product_code_check("jcfIjXiSqQcv`pH4"))
