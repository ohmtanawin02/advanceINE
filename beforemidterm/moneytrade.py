bath = int(input("Enter Your Money [Bath] = "))
print("Your Money is ",bath)
usd = bath//30
penny =((bath/30-usd)*100)//1 
yen = bath//0.28
cen =((bath//0.28-yen))//1                                             
#penny = usd%d

print(bath,"Bath","=",usd,"US Dollar",'%d'%(penny),"Penny ")
print(bath,"Bath","=",bath/0.28,"Yen","Cen")
print(bath,"Bath","=",bath/0.0035,"Kip","Aut")

#print("Penny%.2f"%bath)


