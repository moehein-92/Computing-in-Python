from math import sin, cos, tan, asin, acos, atan2, radians, degrees, sqrt

def find_net_force_from_file(filename):
    fopen = open(filename, "r")
    Hlist = []
    Vlist = []
    for line in fopen:
        x = line.split()
        #print(x)
        int_mag = int(x[0])
        int_angle = int(x[1])
        H = (int_mag*cos(radians(int_angle)))
        Hlist.append(H)
        V = (int_mag*sin(radians(int_angle)))
        Vlist.append(V)
    #print(Hlist)
    #print(Vlist)
    magnitude = round(sqrt(sum(Hlist)**2 + sum(Vlist)**2), 1)
    angle_in_degrees = round(degrees(atan2(sum(Vlist), sum(Hlist))), 1)
    fopen.close()
    return (magnitude, angle_in_degrees)


#If your function works correctly, this will originally
#print: (87.0, 54.4)
print(find_net_force_from_file("a_few_angles.txt"))
