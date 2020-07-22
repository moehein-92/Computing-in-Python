
def write_movie_info(string, aList):
    fwrite = open(string, "w")
    movie_titles = aList[0][0] +" "+ aList[1][0]
    movie_titles = movie_titles.split()
    dic = {}
    star_list = [str(aList[0][1]+" "+aList[0][2]+" "+aList[0][3]+" "+aList[0][4]), str(aList[1][1]+" "+aList[1][2]+" "+aList[1][3]+" "+aList[1][4])]
    dic = dict(zip(movie_titles, star_list))
    print(dic, file = fwrite)
    fwrite.close()
#Each item in the list will be a tuple. The first item of
#every tuple will be the name of a movie. All remaining items
#in the tuple will be names of performers in the movie.
#
#write_movie_info should write the list of movies to the file
#given by the filename using the following format:
#
# Title: Actor 1, Actor 2, Actor 3, etc.
#
#The movies and the actor names should appear in the same
#order as in the original list/tuples.
#
#So, for this list of tuples:
#
# [("Chocolat", "Juliette Binoche", "Judi Dench", "Johnny Depp", "Alfred Molina"),
#  ("Skyfall", "Judi Dench", "Daniel Craig", "Javier Bardem", "Naomie Harris")]
#
#The file printed would look like this:
#
# Chocolat: Juliette Binoche, Judi Dench, Johnny Depp, Alfred Molina
# Skyfall, Judi Dench, Daniel Craig, Javier Bardem, Naomie Harris
#
#HINT: Remember, you can use slicing on tuples just like strings.
#a_tuple[:2], for example, will give you the first two items in a
#tuple. a_tuple[3:] will give you all the items from the one at
#index 3 to the end.

#If your function works correctly, this will originally
#print nothing -- however, it should write the same contents
#as Sample.txt to Test.txt.
movies = [("Chocolat", "Juliette Binoche", "Judi Dench", "Johnny Depp", "Alfred Molina"), ("Skyfall", "Judi Dench", "Daniel Craig", "Javier Bardem", "Naomie Harris")]
write_movie_info("Test.txt", movies)
