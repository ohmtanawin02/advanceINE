number = int(input())
for i in range(1, number+1):
        line1 = ' ' * (number-i) + '*' * (2*i-1)
        print(line1)
for j in range(number,0,-1):
        line = ' ' * (number-j) + '*' * (j-1)
        print(line)