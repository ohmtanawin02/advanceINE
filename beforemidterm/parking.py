hourin = int(input("Enter your hours in park : "))
minin = int(input("Enter your minute in park : "))
hourout = int(input("Enter your park out : "))
minout = int(input("Enter your minute out : "))
hour = hourout-hourin
minute = minout-minin
total = hour * 60
total2 = total + minute
if hourin < 7 or hourin >23 or hourout <7 or hourout > 23 or minin >= 60 or minout >= 60 :
    print("Fail")
elif total2<=15:
    print("0")
elif total2 <60 :
    print("10")
elif total2 <=180 :
    print("30")
elif total2 <240 :
    print("50")
elif total2 <300 :
    print("70")
elif total2 <360 :
    print("90")
elif total2 >360 and total2 <960 :
    print("200")
else :
    print("FAIL")