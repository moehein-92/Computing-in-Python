#Write a function called pivot_library. pivot_library takes
#as input one parameter, a list of 3-tuples. Each tuple in
#the list has three items: the first item is a movie title
#(a string), the second item is the movie's release year (an
#integer), and the third item is the movie's total gross (an
#integer).

# movies = [("Avatar", 2009, 760507625),
#           ("Black Panther", 2018, 699931862)]

# pivot_library(movies)
#   -> {"Avatar": (2009, 760507625),
#       "Black Panther": (2018, 699931862)}

def pivot_library(tuples):
    tup_lst = []
    movies = []
    dic = {}
    for i in tuples:
        tuple = (i[1], i[2])
        tup_lst.append(tuple)
        mov = i[0]
        dic[mov] = tuple

    return dic

#{"Avatar": (2009, 760507625), "Black Panther": (2018, 699931862)}
movies = [("Avatar", 2009, 760507625), ("Black Panther", 2018, 699931862)]
print(pivot_library(movies))
