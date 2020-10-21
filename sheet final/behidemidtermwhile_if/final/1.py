import pickle
import os
person = {}
def lookperson():
    name = ""
    email = ""
    count = 0
    person = {}
    open_file = open('/Users/Python/Desktop/mypython-1/data.txt','r')    
    for i in open_file:
        i = i.split('|')
        for ha in i:
            count = count + 1
            if count == 1:
                name = name + ha
            else:
                count = 0
                person[name] = ha
                name = ""
    open_file.close()
    print(person)
def add():
    output_file = open('/Users/Python/Desktop/mypython-1/data.txt','w')
    person['name'] = input('Name : ')
    person['email'] = input('Email : ')
    output_file.write(str(person))
    output_file.close()
    print(person)
def change():
    print('66')
def delete():
    print(person.popitem())
def main():
    keepgoing = 'y' or 'Y'
    while keepgoing == 'y' or 'Y' :
        print('1.Look up a person')
        print('2.Add a new name and email address')
        print('3.Change and existing email address')
        print('4.Delete an existing name and email address')
        entermenu = int(input('Enter menu : '))
        if entermenu == 1 :
            lookperson()
        elif entermenu == 2 :
            add()
        elif entermenu == 3 :
            change()
        elif entermenu == 4 :
            delete()
        else :
            print('Please select menu !!') 
main()