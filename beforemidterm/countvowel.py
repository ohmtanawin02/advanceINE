count = 0
vowel = 'aeiou'
message = ' '
msg = input('Enter message = ')
for i in msg:
    if not(i in vowel):
        message = message + ' '
    else :
        message = message + i
print(msg)
print(len(msg))
print(message.split())
print(len(message.split()))