hours = int(input("Working Hours: "))
salary = 2000
hourly = 2000 / 8

if hours <= 8:
    print("Your Payment: " + str(salary))
elif hours > 8 and hours <= 10:
    overTime = 1.5 * hourly
    print("Your Payment: " + str(salary + overTime))
else:
    overTime = 1000
    print("Your Payment: " + str(salary + overTime))
