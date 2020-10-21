def main():
    infile1 = open('/Users/Python/Desktop/mypython/mypython-4/behidemidterm/file/A.txt', 'r')
    infile2 = open('/Users/Python/Desktop/mypython/mypython-4/behidemidterm/file/B.txt', 'r')
    outfile = open('/Users/Python/Desktop/mypython/mypython-4/behidemidterm/file/C.txt', 'w')

    num1 = int(infile1.readline())
    num2 = int(infile1.readline())
    num3 = int(infile1.readline())
    num4 = int(infile1.readline())
    a = num1
    b = num2
    c = num3
    d = num4
    ##############################
    num_1 = int(infile2.readline())
    num_2 = int(infile2.readline())
    num_3 = int(infile2.readline())
    num_4 = int(infile2.readline())
    e = num_1
    f = num_2
    g = num_3
    i = num_4
    ##############################
    numtotal1 = a + e
    numtotal2 = b + f
    numtotal3 = c + g
    numtotal4 = d + i
    infile1.close()
    infile2.close()
    #############################
    outfile.write(str(numtotal1) + '\n')
    outfile.write(str(numtotal2) + '\n')
    outfile.write(str(numtotal3) + '\n')
    outfile.write(str(numtotal4) + '\n')
    outfile.close()
main()
    


