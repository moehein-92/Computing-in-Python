#Write a function called sphere_data. sphere_data will
#take in a dictionary. This dictionary is guaranteed to
#have exactly one key: "radius", whose value is an integer
#representing the radius of a sphere.
#
#Modify this dictionary to add two keys: "volume" and "area".
#The values associated with these keys should be the volume
#and surface area of the sphere.
#
from math import pi

def sphere_data(dic):
    radius = dic["radius"]
    volume = round((4/3)*pi*(radius**3), 2)
    area = round(4*pi*(radius**2), 2)
    dic["volume"] = volume
    dic["area"] = area
    return dic


#The formula for volume is:
#  (4/3) * pi * radius ^ 3
#
#The formula for surface area is:
#  4 * pi * radius ^ 2
#
#Both volume and surface area should be rounded to two
#decimal places. You can do this with round(val, 2).
#
#The line below will let you use pi as a variable in your
#code, with a value of pi to the 15th decimal place.

#If your function works correctly, this will originally
#print 4.19 and 12.57, each on a different line.
sphere = {"radius": 1}
sphere = {"radius": 1}
sphere = sphere_data(sphere)
print(sphere["volume"])
print(sphere["area"])
