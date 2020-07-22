driver_speed = 57
speed_limit = 55
school_zone = True

#Write a conditional that decides the price of a speed ticket
#depending on the driver's speed, the speed limit, and
#whether or not they were in a school zone.
#
ini_cost = 100

if driver_speed > speed_limit:
    if school_zone:
        fine = (ini_cost+(10*(driver_speed-speed_limit)))*2
    else:
        fine = (ini_cost+(10*(driver_speed-speed_limit)))
else:
    fine = 0

print("$"+str(fine))
#The reasoning that determines the price of the ticket is:
#
# - $100 for speeding at all (any instance where driver_speed
#   is greater than speed limit).
# - $10 dollars per mile over the speed limit the driver was
#   going.
# - 2x the value otherwise if the violation occurred in a
#   school zone, as represented by the value of school_zone.
#
#Print the cost of the speeding ticket. If the driver was not
#speeding, print $0.
#
#Under the original values above, this should print $240:
#$100 for speeding, $20 for going 2mph above the speed limit,
#and x2 for it occurring in a school zone.


#Add your code here! Make sure to print the dollar sign, too.
