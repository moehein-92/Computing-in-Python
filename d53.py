#In the Pokemon video game series, every Pokemon has six
#stats: HP, Attack, Defense, Special Attack, Special Defense,
#and Speed.
#
#Write a function called total_stats that will take as input
#a list of dictionaries. Each dictionary will have seven
#key-value pairs:

def total_stats(diclist):
    dictionary = {}
    stats_list = []
    pokemons = []
    for i in diclist:
        pokemons.append(i["name"])
        stats = i["hp"]+i["attack"]+i["defense"]+i["special attack"]+i["special defense"]+i["speed"]
        stats_list.append(stats)
    dictionary = dict(zip(pokemons, stats_list))
    return dictionary

#If your function works correctly, this will originally
#print (although the order of the keys may vary):
#{'Bulbasaur': 318, 'Charmander': 309, 'Squirtle': 314}
starters = [{"name": "Bulbasaur", "hp": 45, "attack": 49, "defense": 49, "special attack": 65, "special defense": 65, "speed": 45},
            {"name": "Charmander", "hp": 39, "attack": 52, "defense": 43, "special attack": 60, "special defense": 50, "speed": 65},
            {"name": "Squirtle", "hp": 44, "attack": 48, "defense": 65, "special attack": 50, "special defense": 64, "speed": 43}]
print(total_stats(starters))
