hour = int(input("Enter the number of hour worked : "))
rate = int(input("Enter the hourly pay rate : "))
if hour>40:
   gross =  ((hour-40)*(1.5*rate))+(40*rate)
else :
   gross = hour * rate
print("The gross pay is $",gross)