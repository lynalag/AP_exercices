year = int (input("Enter a year: "))
lp = False
if year % 4 == 0:
    lp = True
    if year%100 == 0 and year%400 != 0: lp = False

if lp: print(year, "is a leap year")
else: print(year, "is not a leap year")