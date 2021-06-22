# %%
#to convert the given date to julian days

from time import ctime
from datetime import date
import calendar

#jan 1 4713 BC 1200 hrs - julian time starts

def getInput():
    
    date_input = input ("Enter date in the form of dd/mm/yyyy: ").split('/')
    day_input = input("Enter the time in 'hr:mm:ss' 12 hrs format: ").split(":")
    meridiem = input("Enter AM/PM: ")
    year = int(date_input[2])
    month = int(date_input[1])
    day = int(date_input[0])
    hour=int(day_input[0])
    minute=int(day_input[1])
    second=int(day_input[2])
    
    return year, month, day, hour, minute, second, meridiem

if __name__ == "__main__":
    
    years, months, days, hours, minutes, seconds, meridien = getInput()
    
    #to calculate the days BC
    bc_days = 0
    for i in range(4714, 1, -1):
        if i == 0:
            break
        elif i%4 == 0: #to check leap year
            bc_days = bc_days + 366
        else:
            bc_days = bc_days+ 365

    #print(bc_days)

    #to calculate the days AD
    julian_days= 0

    for i in range (0, years-1):
        if i%4 == 0:
            julian_days = julian_days + 366
        else:
            julian_days = julian_days + 365

    #print(julian_days)

    #to calculate the number of days in the current mentoned year

    day = 0
    for i in range (0, months-1):
        if i == 9 or 4 or 6 or 11: #months having 30 days 
            day = day + 30 
        elif i == 2:
            if years%4 == 0: #febraury has 29 days in a leap year
                day = day + 29
            else:
                day = day + 28
        else:
            day = day + 31

    # print(days)
    # print(day)

    #calculation for mantissa
    point=0
    if meridien=="AM":
        point = ((hours*60*60) + (minutes*60) + seconds + 43200) #43200 seconds make up 12 hours - 12:00 to 00:00
        day = day - 1 #will be taken into account in seconds from previous day 12 noon
    else:
        point = ((hours*60*60) + (minutes*60) + seconds)

    mantissa = round(point/86400, 5) #86400 is the total number of seconds in 24 hrs i.e., one day 

    '''subract 10 to account for the change over from julian to gregorian calender
    because it did not properly reflect the actual time taken by earth to complete one rotation

    transition happened during the year 1582 '''

    if years >= 1582: 
        final = bc_days + julian_days + days + day + mantissa -10
    else:
        final = bc_days + julian_days + days + day + mantissa

    print(str(final) + " Julian days")




# %%
