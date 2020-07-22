def mult_4(x):
    if len(x)%4 == 0:
        return True
    return False

def is_upper(x):
    for i in x:
        if ord(i)<= 122 and ord(i) >=97:
            return False
    return True

#if (ord(i) <= 90 and ord(i) >= 65):

def A1_appears(x):
    if "A1" in x:
        return True
    return False


#the string is a valid product code, and False if it is not.
def valid_product_code(x):
    if mult_4(x) and is_upper(x) and A1_appears(x):
        return True
    return False

#print(is_upper("ABCD"))
#print: True, True, False, False, False
print(valid_product_code("A12B44BP"))
print(valid_product_code("BFDSAUSA98932RWEFOEWA9FEAA1DSFSF"))
print(valid_product_code("A1BBD5"))
print(valid_product_code("BDD5664S"))
print(valid_product_code("66aBSaA1fdsv"))
