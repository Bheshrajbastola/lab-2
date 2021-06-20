'''9. Check whether the given year is leap year or not. If year is leap print ‘LEAP YEAR’ else print ‘COMMON YEAR’.
Hint: • a year is a leap year if its number is exactly divisible by 4 and is not exactly divisible by 100
• a year is always a leap year if its number is exactly divisible by 400'''

year=int(input("enter a year : "))
if year%4 ==0:
    print("leap year")
elif year%100==0:
    print("not a leap year")
elif year%400==0:
    print("leap year")
else:
    print("not a leap year")

#the years 2000 and 2400 are leap years,
#while 1800, 1900, 2100, 2200, 2300, and 2500 are not leap years.