def interpretCashier(a_string):
    try:
        pin = int(a_string)
        return "PIN"
    except:
        try:
            trans = float(a_string)
            return "Transaction"
        except:
            return "Password"

print(interpretCashier("24.59"))
print(interpretCashier("123456"))
print(interpretCashier("my$up3rs3cur3p4$$w0rd"))
