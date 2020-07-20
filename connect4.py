def check_winner(tuples):

    for total in range(5, -1, -1):
        for count in range(0,7):
            if tuples[total][count:count+4] == ("X", "X", "X", "X"):
                return "X"
            elif tuples[total][count]  == "X" and tuples[total+1][count] == "X"\
                 and tuples[total+2][count] == "X" and tuples[total+3][count] == "X":
                return "X"
            elif tuples[total][count] == "X" and tuples[total+1][count+1] == "X"\
                 and tuples[total+2][count+2] == "X" and tuples[total+3][count+3] == "X":
                return "X"
            elif tuples[total][count+3] == "X" and tuples[total+1][count+2] == "X"\
                 and tuples[total+2][count+1] == "X" and tuples[total+3][count] == "X":
                return "X"
            elif tuples[total-1][count:count+4] == ("O", "O", "O", "O"):
                return "O"
            elif tuples[total][count] == "O" and tuples[total+1][count] == "O"\
                 and tuples[total+2][count] == "O" and tuples[total+3][count] == "O":
                return "O"
            elif tuples[total][count] == "O" and tuples[total+1][count+1] == "O"\
                 and tuples[total+2][count+2] == "O" and tuples[total+3][count+3] == "O":
                return "O"
            elif tuples[total][count+3] == "O" and tuples[total+1][count+2] == "O"\
                 and tuples[total+2][count+1] == "O" and tuples[total+3][count] == "O":
                return "O"
            else:
                return None
#Here are the ways Connect-4 is different from tic-tac-toe:
#
# - Connect-4 is played with 6 rows and 7 columns, not 3
#   rows and 3 columns.
# - You must have 4 in a row (or column or diagonal) to win
#   instead of 3.
# - You may only place pieces in the bottom-most empty
#   space in a column (e.g. you "drop" the pieces in the
#   column and they fall to the first empty spot). Note,
#   though, that this shouldn't affect your reasoning.
#
#To keep things simple, we'll still use "X" and "O" to
#represent the players, and None to represent empty spots.
#You may assume there will be only one winner per board,
#no characters besides "X", "O", and None, and you don't
#have to worry about whether the board is actually a
#valid game of Connect 4.
#
#Hints:
# - Don't forget both kinds of diagonals, top-left to
#   bottom-right and bottom-left to top-right.
# - This board is too large to check every possible place
#   for a winner: there are 69 places a player could win.
# - Remember, if you put a negative index in a list,
#   Python "wraps around" and checks the last value. You
#   may have to control for this.

xwins = ((None, None, None, None, None, None, None),
         (None, None, None, None, None, None, None),
         (None, None, None, None, "X" , None, None),
         (None, None, None, "X" , "O" , "O", None),
         (None, "O" , "X" , "X" , "O" , "X", None),
         ("O" , "X" , "O" , "O" , "O" , "X" , "X"))
owins = ((None, None, None, None, None, None, None),
         (None, None, None, None, None, None, None),
         ("O" , "O" , "O" , "O" , None, None, None),
         ("O" , "X" , "X" , "X" , None, None, None),
         ("X" , "X" , "X" , "O" , "X" , None, None),
         ("X" , "O" , "O" , "X" , "O" , None, None))
nowins =(("X" , "X" , None, None, None, None, None),
         ("O" , "O" , None, None, None, None, None),
         ("O" , "X" , "O" , "O" , None, "O" , "O" ),
         ("O" , "X" , "X" , "X" , None, "X" , "X" ),
         ("X" , "X" , "X" , "O" , "X" , "X" , "O" ),
         ("X" , "O" , "O" , "X" , "O" , "X" , "O" ))

print(check_winner(xwins))
print(check_winner(owins))
print(check_winner(nowins))
