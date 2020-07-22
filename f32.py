days_late = 500
in_demand = True

if days_late <= 10:
    fine = 1*days_late
elif days_late > 10:
    fine = 10+(2*(days_late-10))
elif days_late == 0:
    fine = 0

if in_demand:
    total_fine = fine*2
    print("$"+str(total_fine))
elif not in_demand:
    total_fine = fine
    print("$"+str(total_fine))
else:
    print("$"+str(fine))
