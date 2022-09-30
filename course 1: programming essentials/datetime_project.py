#course 1 project

# author - @raj-ch017

"""
Project for Week 4 of "Python Programming Essentials".
Collection of functions to process dates.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import datetime

def days_in_month(year,month):
    """
   Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    i = 1
    if (month==12):
        year2 = year + 1
        month2 = 1
        x = datetime.date(year,month,i)
        y = datetime.date(year2,month2,i)
        diff = y - x
        return diff.days
    else:
        month2 = month + 1
        x = datetime.date(year,month,i)
        y = datetime.date(year,month2,i)
        diff = y - x 
        return diff.days

#print(days_in_month(2020,2))

def is_valid_date(year,month,day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    if((year < datetime.MINYEAR) or (year > datetime.MAXYEAR) or (month > 12) or (day > 31) or (month < 1) or (day < 1)):
        return False
    x = year
    y = month
    z = day
    j = days_in_month(x,y)
    if (z > j):
        return False
    else:
        return True

#print(is_valid_date(2020,7,32))

def days_between(year1,month1,day1,year2,month2,day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date
      
    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is 
      before the first date.
    """
    if((is_valid_date(year1,month1,day1)) and (is_valid_date(year2,month2,day2))):
        p = datetime.date(year1,month1,day1)
        q = datetime.date(year2,month2,day2)
        diff = (q-p).days
        if (diff < 0):
            return 0
        else:
            return diff
    else:
        return 0

#print(days_between(2022,1,1,2021,4,1))

def age_in_days(year,month,day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid or if the input
      date is in the future.
    """
    t_day = datetime.date.today()
    x = is_valid_date(year,month,day)
    if (x==False):
        return 0
    a = t_day.year
    b = t_day.month
    c = t_day.day
    diff = days_between(year,month,day,a,b,c)
    if (diff < 0):
        return 0
    return diff


print(age_in_days(1999,7,1))
