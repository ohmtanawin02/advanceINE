import pickle
import os

def Display() :
    try :
        input_file = open('email.dat','rb')
        email = pickle.load(input_file)
        for key in email :
            print(key,'email is',email[key])
        input_file.close()
    except IOError :
        print('An error occured trying to read the file')

def Look_up() :
    index = 0
    try :
        input_file = open('email.dat','rb')
        email = pickle.load(input_file)
        elements = len(email)
        name = input('Enter a person name : ')
        for key in email :
            if key == name :
                print('Your email is',email[key])
            else :
                index += 1
        if index == elements :
            print('Not have this name in file')
        input_file.close()
    except IOError :
        print('An error occured trying to read the file')

def Add_new_name() :
    try :
        input_file = open('email.dat','rb')
        output_file = open('add.dat','wb')
        file = pickle.load(input_file)
        name = input('Enter name to Add : ')
        file[name] = input('Enter email : ')
        pickle.dump(file, output_file)
        output_file.close()
        input_file.close()
        os.remove('email.dat')
        os.rename('add.dat','email.dat')
    except IOError :
        print('An error occured trying to read the file')

def Change() :
    index = 0
    try :
        input_file = open('email.dat','rb')
        output_file = open('change.dat','wb')
        file = pickle.load(input_file)
        elements = len(file)
        name = input('Enter name to change :  ')
        email = input('Enter new email : ')
        for key in file :
            if key == name :
                file[key] = email
            else :
                index += 1
        if index == elements :
            print('Not have this name in file')
        pickle.dump(file, output_file)
        output_file.close()
        input_file.close()
        os.remove('email.dat')
        os.rename('change.dat','email.dat')
    except IOError :
        print('An error occured trying to read the file')

def Delete() :
    index = 0
    try :
        input_file = open('email.dat','rb')
        output_file = open('delete.dat','wb')
        file = pickle.load(input_file)
        elements = len(file)
        name = input('Enter name to delete  ')
        for key in file :
            if key == name :
                del file[name]
            else :
                index += 1
        if index == elements :
            print('Not have this name in file')
        pickle.dump(file, output_file)
        output_file.close()
        input_file.close()
        os.remove('email.dat')
        os.rename('delete.dat','email.dat')
    except IOError :
        print('An error occured trying to read the file')

def main() :
    keep_going = 'y'
    while keep_going == 'y' or keep_going == 'Y' :
        try :
            print('1.   Display a menu')
            print('2.   Look up a person email address')
            print('3.   Add a new name and email address')
            print('4.   Change an existing email address')
            print('5.   Delete an existing name and email address')
            choose = int(input('Enter your choose : '))
            if 6 > choose > 0 :
                if choose == 1 :
                    Display()
                if choose == 2 :
                    Look_up()
                if choose == 3 :
                    Add_new_name()
                if choose == 4 :
                    Change()
                if choose == 5 :
                    Delete()
            else :
                print('\n----------| Error |----------\n')
            keep_going = input('Enter y or Y to go : ')
            if keep_going == 'y' or keep_going == 'Y' :
                main()
            else :
                print('\n===========')
                print('Only Y or y')
                print('===========\n')
        except ValueError :
            print('\n==========')
            print('Only Number')
            print('==========\n')
main()
