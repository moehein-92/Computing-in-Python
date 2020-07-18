from math import atan2, degrees, radians, sin, cos

class Force:
    def __init__(self, magnitude, angle):
        self.magnitude = magnitude
        self.angle = angle
    def get_horizontal(self):
        horizontal = self.magnitude*cos(radians(self.angle))
        return horizontal
    def get_vertical(self):
        vertical = self.magnitude*sin(radians(self.angle))
        return vertical
    def get_angle(self, use_degrees = True):
        angle_in_deg = self.angle
        angle_in_rad = radians(angle_in_deg)
        if use_degrees:
            return angle_in_deg
        else:
            return angle_in_rad
def find_net_force(flist):
    hforces = []
    vforces = []
    for force in flist:
        hforce = force.get_horizontal()
        vforce = force.get_vertical()
        hforces.append(hforce)
        vforces.append(vforce)
    net_force = round((sum(hforces)**2 + sum(vforces)**2)**0.5, 1)
    net_angle = round(degrees(atan2(sum(vforces), sum(hforces))), 1)
    return Force(net_force, net_angle)

#If your code works correctly, this will originally run
#error-free and print:
#103.1
#-14.0
force_1 = Force(50, 90)
force_2 = Force(75, -90)
force_3 = Force(100, 0)
forces = [force_1, force_2, force_3]
net_force = find_net_force(forces)
print(net_force.magnitude)
print(net_force.get_angle())
