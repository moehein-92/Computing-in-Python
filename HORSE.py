def check_horse_winner(tuple):
    tlist = list(tuple)
    lst = []
    count = 0
    if all(len(name) < 5 for name in tlist):
        return "Everyone: keep playing!"
    for i, v in enumerate(tlist):
        if len(v) < 5:
            count += 1
            lst.append(str(i))
    #return lst
    if count >= 2:
        s = ", ".join(lst)
        return "Players {0}: keep playing!".format(s)
    elif count < 2:
        return "Player {0} wins!".format(lst[0])

#print(check_horse_winner(("HOR", "HORS", "H", "HO"))) --> "Everyone: keep playing!"
#print(check_horse_winner(("HORSE", "HOR", "HORS", "HORSE"))) --> "Players 1, 2: keep playing!"
#print(check_horse_winner(("HORSE", "HORSE", "HORS", "HORSE"))) --> "Player 2 wins!"
print(check_horse_winner(("HORSE", "HOR", "HORS", "", "HORSE", "H", "HORSE", "HORS", "HORSE")))
#-- > "Players 1, 2, 3, 5, 7: keep playing!"
