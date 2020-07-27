
class Pokemon:
    def __init__(self, Number, Name, Type1, HP, Attack, Defense,
                SpecialAtk, SpecialDef, Speed,Generation, Legendary, Mega, Type2 = ""):

        self.Number = Number
        self.Name = Name
        self.Type1 = Type1
        self.Type2 = Type2
        self.HP = HP
        self.Attack = Attack
        self.Defense = Defense
        self.SpecialAtk = SpecialAtk
        self.SpecialDef = SpecialDef
        self.Speed = Speed
        self.Generation = Generation
        self.Legendary = Legendary
        self.Mega = Mega

    def total_stats(self):
        total = int(self.HP)+int(self.Attack)+int(self.Defense)+int(self.SpecialAtk)
        +int(self.SpecialDef)+int(self.Speed)
        return total

poke_list = []
pokedex = open('../resource/lib/public/pokedex.csv', 'r')
for line in pokedex:
    line = line.strip().split(",")
    poke_list.append(Pokemon(line[0], line[1],line[2],line[4],line[5],line[6],line[7], line[8],line[9],line[10],line[11],line[12],line[3]))


#print(poke_list)
hitpoints = []
for pokemon in poke_list:
    count = 0
    hitpoints.append(pokemon.HP)
    if pokemon.Type2 == "":
        count+=1

for pokemon in poke_list:
    if pokemon.Defense == "230":
        print(pokemon.Name)
#hitpoints.sort()
#print(hitpoints)
dic1 = {}
defen = []
for pokemon in poke_list:
    if pokemon.Legendary == "FALSE":
        if pokemon.Mega == "FALSE":
            defen.append(int(pokemon.Defense))
defen.sort()
#print(defen)
#print(dic1)
legend1 = {}
legend2 = {}
for pokemon in poke_list:
    if pokemon.Legendary == "TRUE":
        if pokemon.Type1 in legend1:
            legend1[pokemon.Type1] += 1
        else:
            legend1[pokemon.Type1] = 1

for pokemon in poke_list:
    if pokemon.Legendary == "TRUE":
        if pokemon.Type2 in legend2:
            legend2[pokemon.Type2] += 1
        else:
            legend2[pokemon.Type2] = 1
#print(legend1)
#print(legend2)

dic2 = {}
for pokemon in poke_list:
    if (pokemon.Type2) in dic2:
        dic2[pokemon.Type2] += 1
    else:
        dic2[pokemon.Type2] = 1
#print(dic2)
stats = {}
for pokemon in poke_list:
    if pokemon.Legendary == "TRUE":
        stats[pokemon.Name] = pokemon.total_stats()
#print(stats)

g7 = []
for pokemon in poke_list:
    if pokemon.Generation == "7":
        g7.append(pokemon.total_stats())
print("g7:", sum(g7)/len(g7))
