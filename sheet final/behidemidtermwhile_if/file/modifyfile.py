import os
def main():
    infile = open('/Users/Python/Desktop/mypython/mypython-4/employees2.txt','r')
    outfile = open('/Users/Python/Desktop/mypython/mypython-4/behidemidterm/file/temp.txt','w') 
    oldname = input('Enter old name : ')
    newname = input('Enter new name : ')
    for line in infile :
        rec = (line.rsplit('|'))
        if rec[0] == oldname :
            outfile.write(newname+'|'+rec[1]+'|'+rec[2])
        else:
            outfile.write(line)
    infile.close()
    outfile.close()

main()

