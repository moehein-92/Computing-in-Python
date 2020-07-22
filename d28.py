#Write a function called average_heart_rate.
#average_heart_rate should have one parameter, a list of
#integers. These integers represent heart rate measurements
#taken 30 seconds apart. average_heart_rate should return
#the average of all heart rates between the first 100+
#heart rate and the last one. Return this as an integer
#(use floor division when calculating the average).

def average_heart_rate(list):
    hrate = []
    for i in list:
        if i >= 100:
            hrate.append(i)
    avg = sum(hrate)//len(hrate)
    return avg


#If your function works correctly, this will originally
#print 114 (because there are 14 measurements from 102 to
#101, their sum is 1609, and 1609 // 14 is 114).
beats = [72, 77, 79, 95, 102, 105, 112, 115, 120, 121, 121,
         125, 125, 123, 119, 115, 105, 101, 96, 92, 90, 85]
print(average_heart_rate(beats))
