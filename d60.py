
#Each line of the file contains six items, separated by commas:
#
# - the transit day, in MM/DD/YYYY format.
# - the transit time, in HH:MM:SS format.
# - the device ID, an identifer of the gate at which the rider entered.
# - the station ID, a numeric identifier the station.
# - the use type, whether the rider was entering, exiting, etc.
# - a serial number, the unique identifier of the rider's Breeze Card.
#
#Your goal is to use this file to answer three questions:
#
# - What is the average number of Breeze Card taps per station?
# - What is the station ID of the station whose traffic is the closest
#   to that average?
# - What station has the least overall amount of traffic?

marta_file = open('../resource/lib/public/marta_01-18-2016.csv', 'r')

station_dict = {}
count = []
for line in marta_file:
    line = line.split(",")
    if not line[3] in station_dict:
        station_dict[line[3]] = 1
    else:
        station_dict[line[3]] += 1

print(station_dict)

for k, v in station_dict.items():
    count.append(v)

avg_taps = sum(count)/len(station_dict)
print(avg_taps)
print(min(count))
