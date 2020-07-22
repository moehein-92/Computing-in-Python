import math

def solve_right_triangle(opposite, adjacent, use_degrees = False):
    hypotenuse = ((opposite**2)+(adjacent**2))**0.5
    angle = math.atan(opposite/adjacent)
    if use_degrees == True:
        angle = math.degrees(angle)
    return (hypotenuse, angle)


#If your function works correctly, this will originally
#print:
#(5.0, 0.6435011087932844)
#(5.0, 36.86989764584402)
print(solve_right_triangle(3.0, 4.0))
print(solve_right_triangle(3.0, 4.0, use_degrees = True))
