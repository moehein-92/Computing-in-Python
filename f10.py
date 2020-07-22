def calculate_modifier(STAB, Type, Critical, Other, Random):
    modifier = float(STAB)*float(Type)*float(Critical)*float(Other)*float(Random)
    return modifier


def calculate_damage(STAB, Type, Critical, Other, Random, Level, Attack,
                    Defense, Base):
    Damage = ((((2*float(Level))+10)/250)*(float(Attack)/float(Defense))*(float(Base))+2)\
            *calculate_modifier(STAB, Type, Critical, Other, Random)
    return Damage


STAB = 1
Type = 0.25
Critical = 2
Other = 1
Random = 1
Level = 50
Attack = 125
Defense = 110
Base = 60

print(calculate_damage(STAB, Type, Critical, Other, Random, Level, Attack, Defense, Base))
