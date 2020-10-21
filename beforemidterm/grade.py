name = input("Enter name : ")
score = int(input("Enter score : "))
if score >= 80:
    print("A")
elif score >= 75:
    print("B+")
elif score >=70:
    print("B")
elif score >=65:
    print("C+")
elif score >=60:
    print("C")
elif score >=55:
    print("D+")
elif score >=50:
    print("D")
elif score <=49:
    print("F")
else:
    print("No Grade !!")
      