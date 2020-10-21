def main():
    infile1 = open('/Users/Python/Desktop/mypython/mypython-4/behidemidterm/file/LA.txt', 'r')
    infile2 = open('/Users/Python/Desktop/mypython/mypython-4/behidemidterm/file/LB.txt', 'r')
    outfile = open('/Users/Python/Desktop/mypython/mypython-4/behidemidterm/file/LC.txt', 'w')
    for line1 in infile1:
        avalue = float(line1)
        bvalue = float(infile2.readline())
        total = avalue + bvalue
        print(format(avalue,'.2f'))
        print(format(bvalue,'.2f'))
        outfile.write(str(total)+'\n')
        
         
    infile1.close()
    infile2.close()
    outfile.close()
main()