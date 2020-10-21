def main():
    infile = open('/Users/Python/Desktop/mypython/mypython-4/employees2.txt','r')
    for line in infile :
        line = line.split("|")
        print("Name",line[0])
        print("ID",line[1])
        print("Dept",line[2])
    infile.close
main()

