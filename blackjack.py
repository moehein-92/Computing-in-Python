def next_move(string):
    total = 0
    tens = {"J":10, "K":10, "Q":10}
    num = [2, 3, 4, 5, 6, 7, 8, 9]

    for i in string:
        if i == "0":
            total += 10
        if i in tens:
            total += tens[i]
        try:
            if int(i) in num:
                total += int(i)
        except:
            pass
        else:
            if i == "A":
                if total <= 10:
                    total += 11
                else:
                    total += 1
    #print(total)
    if total < 17:
        return "Hit"
    elif total >= 17 and total <= 21:
        return "Stay"
    elif total > 21:
        return "Bust"


#If your function works correctly, this will originally
#print: Hit, Hit, Stay, and Bust.

print(next_move("04J"))
print(next_move("A3"))
print(next_move("A39"))
print(next_move("A397"))
print(next_move("A397K"))
