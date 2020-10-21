setA = {1,2,3,4,5,6,7,8}
setB = {6,7,8,9,10,('A,B,C,D')}
setC = {4,5,7,8,10,('A,B,C,D,X,Y,Z')}
print(setA)
print(setB)
print(setC)
print(setA & setB & setC)
print(setA & setB - setC)
print(setA & setB & setC ^ setC - setA)