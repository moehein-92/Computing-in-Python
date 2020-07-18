#Copy your Burrito class from the last exercise. Below,
#We've given you three additional classes named "Meat",
#"Rice" and "Beans." We've gone ahead and built getters
#and setters in these classes to check if the incoming
#values are valid, so you'll be able to remove those
#from your original code.
#
class Burrito:
    def __init__(self, meat, to_go, rice, beans, extra_meat = False, guacamole = False,\
                cheese = False, pico = False, corn = False):

        self.meat = Meat(meat)
        self.set_to_go(to_go)
        self.rice = Rice(rice)
        self.beans = Beans(beans)
        self.set_extra_meat(extra_meat)
        self.set_cheese(cheese)
        self.set_pico(pico)
        self.set_corn(corn)
        self.set_guacamole(guacamole)

    def get_meat(self):
        return self.meat
    def set_meat(self, meat):
        self.meat = meat
    def get_beans(self):
        return self.beans
    def set_beans(self, beans):
        self.beans = beans
    def get_rice(self):
        return self.rice
    def set_rice(self, rice):
        self.rice = rice

    def get_to_go(self):
        return self.to_go
    def set_to_go(self, to_go):
        valid_to_go = [True, False]
        if to_go in valid_to_go:
            self.to_go = to_go
        else:
            self.to_go = False

    def get_extra_meat(self):
        return self.extra_meat
    def set_extra_meat(self, extra_meat):
        valid_extra_meat = [True, False]
        if extra_meat in valid_extra_meat:
            self.extra_meat = extra_meat
        else:
            self.extra_meat = False

    def get_guacamole(self):
        return self.guacamole
    def set_guacamole(self, guacamole):
        valid_guacamole = [True, False]
        if guacamole in valid_guacamole:
            self.guacamole = guacamole
        else:
            self.guacamole = False

    def get_cheese(self):
        return self.cheese
    def set_cheese(self, cheese):
        valid_cheese = [True, False]
        if cheese in valid_cheese:
            self.cheese = cheese
        else:
            self.cheese = False

    def get_pico(self):
        return self.pico
    def set_pico(self, pico):
        valid_pico = [True, False]
        if pico in valid_pico:
            self.pico = pico
        else:
            self.pico = False

    def get_corn(self):
        return self.corn
    def set_corn(self, corn):
        valid_corn = [True, False]
        if corn in valid_corn:
            self.corn = corn
        else:
            self.corn = False

    def get_cost(self):
        cost = 5.0
        if self.get_meat() in ["chicken", "pork", "tofu"]:
            cost += 1
        if self.get_meat() == "steak":
            cost += 1.5
        if self.get_extra_meat() == True and not self.get_meat() == False:
            cost += 1
        if self.get_guacamole() == True:
            cost += 0.75
        return cost

class Meat:
    def __init__(self, value=False):
        self.set_value(value)
    def get_value(self):
        return self.value
    def set_value(self, value):
        if value in ["chicken", "pork", "steak", "tofu"]:
            self.value = value
        else:
            self.value = False

class Rice:
    def __init__(self, value=False):
        self.set_value(value)
    def get_value(self):
        return self.value
    def set_value(self, value):
        if value in ["brown", "white"]:
            self.value = value
        else:
            self.value = False

class Beans:
    def __init__(self, value=False):
        self.set_value(value)
    def get_value(self):
        return self.value
    def set_value(self, value):
        if value in ["black", "pinto"]:
            self.value = value
        else:
            self.value = False

a_burrito = Burrito("pork", False, "white", "black", extra_meat = True, guacamole = True)
print(a_burrito.get_cost())
