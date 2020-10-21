print("Please select operation -")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
opera = int(input("Select operation form 1,2,3,4 : "))
number1 = int(input("Enter first number : "))
number2 = int(input("Enter second number : "))
if opera==1:
    total = number1+number2
    print(number1,"+",number2,"=",total)
elif opera==2:
    total = number1-number2
    print(number1,"-",number2,"=",total)
elif opera==3:
    total = number1*number2
    print(number1,"*",number2,"=",total)
elif opera==4:
    total = number1/number2
    print(number1,"/",number2,"=",total)
else:
    print("ERROR!")

