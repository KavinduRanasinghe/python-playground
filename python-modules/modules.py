import sys

locations = sys.path

print(locations)


for location in locations:
    print(location,"\n")
    pass




import calendar
fromY=2000
toY=2050
n_leap_years = calendar.leapdays(fromY,toY)

print("From {} to {} , {} years are there".format(fromY,toY,n_leap_years))
