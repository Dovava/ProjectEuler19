months = [31,28,31,30,31,30,31,31,30,31,30,31]
sundays = 0
day_count = -2
for year in range(1901,2002):
    if year % 4 == 0 and not (year % 400 == 0):
        months[1] = 29
    else:
        months[1] = 28
    for month in range(1,13):
        for day in range(1,months[month-1]+1):
            if day_count % 7 == 0 and day == 1:
                sundays += 1

            day_count += 1

print(sundays)
