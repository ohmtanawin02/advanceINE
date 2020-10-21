year = int(input("Enter a year : "))
if (year % 100) == 0:
    if (year % 400) == 0:
        day = "29"
    else:
        day = "28"
else:
    if (year % 4) == 0:
        day = "29"
    else:
        day = "28"
print("In",year,"Febuary has",day,"days")