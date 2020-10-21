num = int(input("Enter ISBM : "))
m9 = num%10
m8 = (num//10)%10
m7 = (num//100)%10
m6 = (num//1000)%10
m5 = (num//10000)%10
m4 = (num//100000)%10
m3 = (num//1000000)%10
m2 = (num//10000000)%10
m1 = (num//100000000)%10
cal = (10*m1)+(9*m2)+(8*m3)+(7*m4)+(6*m5)+(5*m6)+(4*m7)+(3*m8)+(2*m9)
cal1 = cal%11
cal2 =cal+cal1
d =cal2%11
s =cal2 -d
result = cal1 - d
print("ISBM : ",m1,m2,m3,m4,m5,m6,m7,m8,m9,result)