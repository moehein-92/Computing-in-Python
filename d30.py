from math import sin, cos, tan, asin, acos, atan2, radians, degrees, sqrt

def find_net_force(tlist):
    Hlist = []
    Vlist = []
    for tuples in tlist:
        H = tuples[0]*cos(radians(tuples[1]))
        Hlist.append(H)
        V = tuples[0]*sin(radians(tuples[1]))
        Vlist.append(V)
    magnitude = round(sqrt(sum(Hlist)**2 + sum(Vlist)**2), 1)
    angle_in_degrees = round(degrees(atan2(sum(Vlist), sum(Hlist))), 1)
    return (magnitude, angle_in_degrees)


#Note that sin, cos, and tan all assume the angle is in
#radians, and asin, acos, and atan2 will all return an
#angle in radians. So, you'll need to convert your angles to
#radians before or after using these functions, using things
#like this: angle_in_radians = radians(angle)
#           angle_in_degrees = degrees(angle_in_radians)


#If your function works correctly, this will originally
#print: (87.0, 54.4)

forces = [(10, 90), (10, -90), (100, 45), (20, 180)]
print(find_net_force(forces))
