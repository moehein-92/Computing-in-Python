class Burrito:
    def __init__(self, meat, to_go, rice, beans, extra_meat = False, guacamole = False,\
                cheese = False, pico = False, corn = False):

        self.set_meat(meat)
        self.set_to_go(to_go)
        self.set_rice(rice)
        self.set_beans(beans)
        self.set_extra_meat(extra_meat)
        self.set_cheese(cheese)
        self.set_pico(pico)
        self.set_corn(corn)
        self.set_guacamole(guacamole)

    def get_meat(self):
        return self.meat
    def get_to_go(self):
        return self.to_go
    def get_rice(self):
        return self.rice
    def get_beans(self):
        return self.beans
    def get_extra_meat(self):
        return self.extra_meat
    def get_guacamole(self):
        return self.guacamole
    def get_cheese(self):
        return self.cheese
    def get_pico(self):
        return self.pico
    def get_corn(self):
        return self.corn
    def set_meat(self, meat):
        valid_meat = ["chicken", "pork", "steak", "tofu", False]
        if meat in valid_meat:
            self.meat = meat
        else:
            self.meat = False
    def set_to_go(self, to_go):
        valid_to_go = [True, False]
        if to_go in valid_to_go:
            self.to_go = to_go
        else:
            self.to_go = False
    def set_rice(self, rice):
        valid_rice = ["brown", "white", False]
        if rice in valid_rice:
            self.rice = rice
        else:
            self.rice = False
    def set_beans(self, beans):
        valid_beans = ["black", "pinto", False]
        if beans in valid_beans:
            self.beans = beans
        else:
            self.beans = False
    def set_extra_meat(self, extra_meat):
        valid_extra_meat = [True, False]
        if extra_meat in valid_extra_meat:
            self.extra_meat = extra_meat
        else:
            self.extra_meat = False
    def set_guacamole(self, guacamole):
        valid_guacamole = [True, False]
        if guacamole in valid_guacamole:
            self.guacamole = guacamole
        else:
            self.guacamole = False
    def set_cheese(self, cheese):
        valid_cheese = [True, False]
        if cheese in valid_cheese:
            self.cheese = cheese
        else:
            self.cheese = False
    def set_pico(self, pico):
        valid_pico = [True, False]
        if pico in valid_pico:
            self.pico = pico
        else:
            self.pico = False
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

a_burrito = Burrito("pork", False, "white", "black", extra_meat = True, guacamole = True)
print(a_burrito.get_cost())
print(a_burrito.get_cheese())
