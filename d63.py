#Write a function called write_movie_info. write_movie_info
#will take as input two parameters: a string and a
#dictionary.
#The string will represent the filename to which to write.
def write_movie_info(string, dic):
    fwrite = open(string, "w")
    star_list = list(dic.values())
    #star_list.sort()
    star_string_list = []
    movie_list = list(dic.keys())
    #movie_list.sort()
    for i in star_list:
        text = ", ".join(i)
        star_string_list.append(text)
    dic = {}
    for j in movie_list:
        dic = dict(zip(movie_list, star_string_list))

    for (k, v) in dic.items():
        print(k+": "+v, file = fwrite)
    fwrite.close()

#The file printed would look like this:
# Chocolat: Alfred Molina, Johnny Depp, Judi Dench, Juliette Binoche
# Skyfall: Daniel Craig, Javier Bardem, Judi Dench, Naomie Harris

movies = {"Chocolat": ["Juliette Binoche", "Judi Dench", "Johnny Depp", "Alfred Molina"], "Skyfall": ["Judi Dench", "Daniel Craig", "Javier Bardem", "Naomie Harris"]}
write_movie_info("Test.txt", movies)
