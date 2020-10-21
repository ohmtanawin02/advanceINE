num = int(input(""))
for i in range(num):
    print(''*(num-i-1)+'* '*(i+1))
for j in range(num-1,0,-1):
    print(''*(num-j)+'* '*(j))
#for i in range(0,num):
    #for j in range(0,num-i-1):
    #    print(end=" ")
    #for j in range(0,2*i+1):
    #    print("*",end="")
    #for j in range(0,num,-2):
    #    print("*",end="")
    #print()