#สร้างDictionnary
phonebook = {'Anirach': '777-1111','Mickey':'777-2222','Donald':'777-3333'}

print(phonebook)

#เรียกค่า key example = Mickey || 777-2222
print(phonebook['Mickey'])
print(phonebook.get('Donald'))

key = 'Pluto'
#add sum dictionnary
phonebook['Simpson'] = '777-4567'
phonebook['Pluto'] = '777-4444'
phonebook['Mickey'] = '777-2122'
print(phonebook)

#dele Simpson in dictionnary
del phonebook['Simpson']
print(phonebook)

if key in phonebook:
    print(phonebook['Pluto'])
else:
    print(key + ' not in phonebook')
elements = len(phonebook)
print(elements)
