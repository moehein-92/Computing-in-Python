
def all_time_record(string):
    record_file = open('../resource/lib/public/georgia_tech_football.csv', 'r')
    wins = 0
    losses = 0
    ties = 0
    year_list = list(range(1933, 1964))
    print(year_list)
    for line in record_file:
        data = line.strip().split(",")
        #print(data)
        try:
            if int(data[0][0:4]) in year_list:
                if data[3] == data[4]:
                    ties += 1
                elif int(data[3]) > int(data[4]):
                    wins += 1
                elif int(data[3]) < int(data[4]):
                    losses += 1
        except:
            pass


    output = "{0}-{1}-{2}".format(wins, losses, ties)
    record_file.close()
    return output

print(all_time_record("Auburn"))
