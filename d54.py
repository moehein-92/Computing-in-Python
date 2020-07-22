#Write a function called population_density. The function
#should take one parameter, which will be a list of
#dictionaries. Each dictionary in the list will have three
#key-value pairs:

def population_density(dictlist):
    pop_list = []
    area_list = []
    for dic in dictlist:
        pop = int(dic["population"])
        pop_list.append(pop)
        area = int(dic["area"])
        area_list.append(area)
    density = round(sum(pop_list)/sum(area_list), 3)
    return density


#If your function works correctly, this will originally
#print: 133.886 (or something around there)
countries = [{"name": "China", "population": 1390700000, "area": 9640821},
             {"name": "India", "population": 1348003000, "area": 3287240},
             {"name": "United States", "population": 325300000, "area": 9826675},
             {"name": "Indonesia", "population": 237556363, "area": 1904569}]
print(population_density(countries))
