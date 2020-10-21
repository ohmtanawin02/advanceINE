def main():
    word=''
    count = 0
    infile = open('/Users/Python/Desktop/mypython/mypython-4/employees.txt','r')
    for line in infile :
        count = count + 1
        if count == 1:
            word = word + line
        else:
            word = word +':'+line
        if (count % 3) == 0 :
            word = word.split(':')
            print("Name:",word[0])
            print("ID:",word[1])
            print("Department:",word[2])
            count = 0
            word =""
    infile.close
main()

